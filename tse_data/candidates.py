def candidates(year, position_el = None, round_el = None, cand_situation = None, status = None):
    '''Download and clean data on candidate profiles in Brazilian elections

    :param year: The required year. Choose an option between 2004, 2006, 2008, 2010, 2012, 2014, 2016 and 2018.
    :param position_el: The position that the candidate is applying for. Choose an option between:
            "prefeito" for Mayor;
            "vice-prefeito" for vice Mayor;
            "vereador" for Alderman;
            "governador" for Governor;
            "vice-governador" for vice Governor;
            "presidente" for president;
            "deputado estadual" for state deputy;
            "deputado federal" for Congressman
            "senador" for senator.
    :param round_el: The round of the especific election. Choose 1 for round one and two for round 2.
    :param cand_situation:
    :param status:
    :return: A data frame with informations on candidate profilies.

    '''
    from pandas import DataFrame, read_csv, concat
    from sys import exit
    import requests, zipfile, os

    link = f'http://agencia.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_{year}.zip'

    nomes_cand_12 = ['DATA_GERACAO', 'HORA_GERACAO', 'ANO_ELEICAO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF',
                        'SIGLA_UE',
                        'DESCRICAO_UE', 'CODIGO_CARGO', 'DESCRICAO_CARGO', 'NOME_CANDIDATO', 'SEQUENCIAL_CANDIDATO',
                        'NUMERO_CANDIDATO', 'CPF_CANDIDATO', 'NOME_URNA_CANDIDATO', 'COD_SITUACAO_CANDIDATURA',
                        'DES_SITUACAO_CANDIDATURA', 'NUMERO_PARTIDO', 'SIGLA_PARTIDO', 'NOME_PARTIDO', 'CODIGO_LEGENDA',
                        'SIGLA_LEGENDA', 'COMPOSICAO_LEGENDA', 'NOME_LEGENDA', 'CODIGO_OCUPACAO', 'DESCRICAO_OCUPACAO',
                        'DATA_NASCIMENTO', 'NUM_TITULO_ELEITORAL_CANDIDATO', 'IDADE_DATA_ELEICAO', 'CODIGO_SEXO',
                        'DESCRICAO_SEXO',
                        'COD_GRAU_INSTRUCAO', 'DESCRICAO_GRAU_INSTRUCAO', 'CODIGO_ESTADO_CIVIL',
                        'DESCRICAO_ESTADO_CIVIL',
                        'CODIGO_NACIONALIDADE', 'DESCRICAO_NACIONALIDADE', 'SIGLA_UF_NASCIMENTO',
                        'CODIGO_MUNICIPIO_NASCIMENTO',
                        'NOME_MUNICIPIO_NASCIMENTO', 'DESPESA_MAX_CAMPANHA', 'COD_SIT_TOT_TURNO', 'DESC_SIT_TOT_TURNO',
                        'NM_EMAIL']
    nomes_cand_14_18 = ['DATA_GERACAO', 'HORA_GERACAO', 'ANO_ELEICAO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF',
                           'SIGLA_UE',
                           'DESCRICAO_UE', 'CODIGO_CARGO', 'DESCRICAO_CARGO', 'NOME_CANDIDATO', 'SEQUENCIAL_CANDIDATO',
                           'NUMERO_CANDIDATO', 'CPF_CANDIDATO', 'NOME_URNA_CANDIDATO', 'COD_SITUACAO_CANDIDATURA',
                           'DES_SITUACAO_CANDIDATURA', 'NUMERO_PARTIDO', 'SIGLA_PARTIDO', 'NOME_PARTIDO',
                           'CODIGO_LEGENDA',
                           'SIGLA_LEGENDA', 'COMPOSICAO_LEGENDA', 'NOME_LEGENDA', 'CODIGO_OCUPACAO',
                           'DESCRICAO_OCUPACAO',
                           'DATA_NASCIMENTO', 'NUM_TITULO_ELEITORAL_CANDIDATO', 'IDADE_DATA_ELEICAO', 'CODIGO_SEXO',
                           'DESCRICAO_SEXO',
                           'COD_GRAU_INSTRUCAO', 'DESCRICAO_GRAU_INSTRUCAO', 'CODIGO_ESTADO_CIVIL',
                           'DESCRICAO_ESTADO_CIVIL',
                           'CODIGO_COR_RACA', 'DESCRICAO_COR_RACA', 'CODIGO_NACIONALIDADE', 'DESCRICAO_NACIONALIDADE',
                           'SIGLA_UF_NASCIMENTO', 'CODIGO_MUNICIPIO_NASCIMENTO', 'NOME_MUNICIPIO_NASCIMENTO',
                           'DESPESA_MAX_CAMPANHA',
                           'COD_SIT_TOT_TURNO', 'DESC_SIT_TOT_TURNO', 'NM_EMAIL']
    list_results = list()
    if year not in list(range(2004, 2019, 2)):
        exit("Pleace, choose a valid year!")
    else:
        if year in [2004, 2017, 4] and position_el is None == False and position_el not in ['prefeito', 'vice-prefeito', 'vereador'] or year in [2006, 2019, 4] and position_el is None == False and position_el not in ['governador', 'vice-governador', 'presidente', 'vice_presidente', 'deputado_federal', 'deputado_estadual', 'senador']:
            exit(f"The position_el required is not valid to the year {year}")
        if position_el is None == False:
            if position_el not in ['prefeito', 'vice-prefeito', 'vereador', 'governador', 'vice-governador', 'presidente', 'vice_presidente', 'deputado_federal', 'deputado_estadual', 'senador']:
                exit("Pleace, choose a valid value to the position_el parameter!")
        if round_el is None == False:
            if round_el not in [1, 2]:
                exit("Please, choose a value between 1 and 2 to the parameter round_el")
        if cand_situation is None == False:
            if cand_situation not in ['deferido', 'deferido com recurso', 'indeferido', 'indeferido com recurso']:
                exit("Please, choose an alternative between (deferido, deferido com recurso, indeferido, indeferido com recurso) to parameter cand_situation")
        if status is None == False:
            if status not in ['eleito', 'Não eleito', 'suplente']:
                exit("Please, choose a valid value to parameter status!")

        print("Please, wait for data processing!")
        response = requests.get(link, stream=True)
        target_path = f'consulta_cand_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        for uf in ['AC', 'AM', 'PA', 'RO', 'RR', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'ES', 'MG', 'SP', 'RJ', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO']:
            if year in list(range(2004,2013,2)):
                list_results.append(read_csv(zipfile.ZipFile(f"consulta_cand_{year}.zip", "r").extract(f"consulta_cand_{year}_{uf}.txt"), encoding='latin1', sep=';', names = nomes_cand_12))
            elif year in list(range(2014, 2019, 2)):
                list_results.append(read_csv(zipfile.ZipFile(f"consulta_cand_{year}.zip", "r").extract(f"consulta_cand_{year}_{uf}.txt"), encoding='latin1', sep=';', names=nomes_cand_14_18))
            else:
                exit("Please, enter a valid year!")
            os.remove(f"consulta_cand_{year}_{uf}.txt", "LEIAME.pdf", "consulta_cand_{year}.zip")
        df = DataFrame(concat(
            [list_results[0], list_results[1], list_results[2], list_results[3], list_results[4], list_results[5],
             list_results[6], list_results[7], list_results[8], list_results[9], list_results[10], list_results[11],
             list_results[12], list_results[13], list_results[14], list_results[15], list_results[16], list_results[17],
             list_results[18], list_results[19], list_results[20], list_results[21], list_results[22], list_results[23],
             list_results[24], list_results[25]]))

        if position_el is None == False:
            df = df.lock[df['DESCRICAO_CARGO'] == position_el.upper(), :]
        if round_el is None == False:
            df = df.loc[df['NUM_TURNO'] == round_el, :]
        if cand_situation is None == False:
            df = df.loc[df['DESC_SIT_CANDIDATO'] == cand_situation.upper(), :]
        if status is None == False:
            df = df.loc[df['DESC_SIT_CAND_TOT'] == status.upper(), :]
        return df