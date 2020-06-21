def results(year, position_el = None, round_el = None, cand_situation = None, status = None):
    '''
    :param year: The year required. Choose an year between 2004, 2006, 2008, 2010, 2012, 2014, 2016 and 2018.
    :param position_el: position_el: The position that the candidate is applying for. Choose an option between:
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
    :param cand_situation: The candidate application status. Choose an optino between:
            "deferido" for accepted applications;
            "deferido com recurso" for approved with appeal applications;
             "indeferido"  for rejected applications;
             "indeferido com recurso" for rejected with appeal applications.
    :param status:
    :return:
    '''

    from pandas import DataFrame, read_csv, concat
    from sys import exit
    import requests, zipfile, os

    nomes_res_04_12 = ['DATA_GERACAO', 'HORA_GERACAO', 'ANO_ELEICAO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF',
                          'SIGLA_UE', 'CODIGO_MUNICIPIO', 'NOME_MUNICIPIO', 'NUMERO_ZONA', 'CODIGO_CARGO', 'NUMERO_CAND',
                          'SQ_CANDIDATO', 'NOME_CANDIDATO', 'NOME_URNA_CANDIDATO', 'DESCRICAO_CARGO', 'COD_SIT_CAND_SUPERIOR',
                          'DESC_SIT_CAND_SUPERIOR', 'CODIGO_SIT_CANDIDATO', 'DESC_SIT_CANDIDATO', 'CODIGO_SIT_CAND_TOT', 'DESC_SIT_CAND_TOT',
                          'NUMERO_PARTIDO', 'SIGLA_PARTIDO', 'NOME_PARTIDO', 'SEQUENCIAL_LEGENDA', 'NOME_COLIGACAO', 'COMPOSICAO_LEGENDA', 'TOTAL_VOTOS']
    nomes_res_14_18 = ['DATA_GERACAO', 'HORA_GERACAO', 'ANO_ELEICAO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF',
                          'SIGLA_UE', 'CODIGO_MUNICIPIO', 'NOME_MUNICIPIO', 'NUMERO_ZONA', 'CODIGO_CARGO', 'NUMERO_CAND',
                          'SQ_CANDIDATO', 'NOME_CANDIDATO', 'NOME_URNA_CANDIDATO', 'DESCRICAO_CARGO', 'COD_SIT_CAND_SUPERIOR',
                          'DESC_SIT_CAND_SUPERIOR', 'CODIGO_SIT_CANDIDATO', 'DESC_SIT_CANDIDATO', 'CODIGO_SIT_CAND_TOT', 'DESC_SIT_CAND_TOT',
                          'NUMERO_PARTIDO', 'SIGLA_PARTIDO', 'NOME_PARTIDO', 'SEQUENCIAL_LEGENDA', 'NOME_COLIGACAO', 'COMPOSICAO_LEGENDA', 'TOTAL_VOTOS', "TRANSITO"]

    list_results = list()
    link = f'http://agencia.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_{year}.zip'
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
        target_path = f'votacao_candidato_munzona_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        for uf in ['AC', 'AM', 'PA', 'RO', 'RR', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'ES', 'MG', 'SP', 'RJ', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO']:
            if year in list(range(2004,2013,2)):
                list_results.append(read_csv(zipfile.ZipFile(f"votacao_candidato_munzona_{year}.zip", "r").extract(f"votacao_candidato_munzona_{year}_{uf}.txt"), encoding='latin1', sep=';', names = nomes_res_04_12))
            elif year in list(range(2014, 2019, 2)):
                list_results.append(read_csv(zipfile.ZipFile(f"votacao_candidato_munzona_{year}.zip", "r").extract(f"votacao_candidato_munzona_{year}_{uf}.txt"), encoding='latin1', sep=';', names=nomes_res_14_18))
            else:
                exit("Please, enter a valid year!")
            os.remove(f"votacao_candidato_munzona_{year}_{uf}.txt", "LEIAME.pdf", "votacao_candidato_munzona_{year}.zip")
        df = DataFrame(concat([list_results[0], list_results[1], list_results[2], list_results[3], list_results[4], list_results[5], list_results[6], list_results[7], list_results[8], list_results[9], list_results[10], list_results[11], list_results[12], list_results[13], list_results[14], list_results[15], list_results[16], list_results[17], list_results[18], list_results[19], list_results[20], list_results[21], list_results[22], list_results[23], list_results[24], list_results[25]]))

        if position_el is None == False:
            df = df.lock[df['DESCRICAO_CARGO'] == position_el.upper(), :]
        if round_el is None == False:
            df = df.loc[df['NUM_TURNO'] == round_el, :]
        if cand_situation is None == False:
            df = df.loc[df['DESC_SIT_CANDIDATO'] == cand_situation.upper(), :]
        if status is None == False:
            df = df.loc[df['DESC_SIT_CAND_TOT'] == status.upper(), :]
        return df
