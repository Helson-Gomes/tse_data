def accountabilities(year, type_data = None, type_agent = None):
    '''Download data on candidates and committees accountabilities in Brazilian elections \n
    \n
    Example
    ----------
    \n
    df = accountabilities(year = 2008, type_data = "expends", type_agent = "candidates", sum_ = False)
    \n
    Parameters
    ----------
    :param year: The year required. Choose an year between 2008, 2010, 2012, 2014, 2016 and 2018.
    :param type_data: The type of data required. Choose an option between "revenues" and "expends".
    :param type_agent: Choose "candidates" if you want to download candidates accountabilities or "committees" if you want to download committees accountabilities.
    :return: A data frame with informations on candidates and committees accountabilities in Brazilian elections.


    '''

    from pandas import DataFrame, read_csv, concat
    from sys import exit
    import requests, zipfile, os

    if type_data is None == False and type_data not in ["revenues", "expends"]:
        exit("Please, enter a valid value to parameter type_data!")

    if type_agent is None == False and type_agent not in ["candidates", "committees"]:
        exit("Please, enter a valid value to parameter type_agent!")

    if year not in list(range(2008, 2019, 2)):
        exit("Please, enter a valid year!")

    if year == 2008:
        link = f"http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_{year}.zip"

        print("Please, wait for data processing!")
        response = requests.get(link, stream=True)
        target_path = f'prestacao_contas_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        if type_agent == "candidates":
            type_agent = "candidatos"
        if type_agent == "committiees":
            type_agent = "comites"
        if type_data == "revenues":
            type_data = "receitas"
        if type_data == "expends":
            type_data = "despesas"
        df = DataFrame(read_csv(zipfile.ZipFile(f"prestacao_contas_{year}.zip", "r").extract(f"{type_data}_{type_agent}_{year}_brasil.csv"),
                encoding='latin1', sep=';'))
        os.remove(f"prestacao_contas_{year}.zip", f"{type_data}_{type_agent}_{year}_brasil.csv")


    if year == 2010:
        list_results = []
        link = f"http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_{year}.zip"
        print("Please, wait for data processing!")
        response = requests.get(link, stream=True)
        target_path = f'prestacao_contas_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        for uf in ['AC', 'AM', 'PA', 'RO', 'RR', 'AP', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA', 'ES',
                   'MG', 'SP', 'RJ', 'PR', 'SC', 'RS', 'MS', 'MT', 'GO']:
            if type_agent == "candidates" and type_data == "expends":
                list_results.append((read_csv(zipfile.ZipFile(f"prestacao_contas_{year}.zip", "r").extract(f"/candidato/{uf}/DespesasCandidatos.txt"), encoding='latin1', sep=';')))
            if type_agent == "candidates" and type_data == "revenues":
                list_results.append((read_csv(zipfile.ZipFile(f"prestacao_contas_{year}.zip", "r").extract(f"/candidato/{uf}/ReceitasCandidatos.txt"), encoding='latin1', sep=';')))
            if type_agent == "committees" and type_data == "expends":
                list_results.append((read_csv(zipfile.ZipFile(f"prestacao_contas_{year}.zip", "r").extract(f"/comite/{uf}/DespesasCandidatos.txt"), encoding='latin1', sep=';')))
            if type_agent == "committees" and type_data == "revenues":
                list_results.append((read_csv(zipfile.ZipFile(f"prestacao_contas_{year}.zip", "r").extract(f"/comite/{uf}/ReceitasCandidatos.txt"), encoding='latin1', sep=';')))
            df = DataFrame(concat(
                [list_results[0], list_results[1], list_results[2], list_results[3], list_results[4], list_results[5],
                 list_results[6], list_results[7], list_results[8], list_results[9], list_results[10], list_results[11],
                 list_results[12], list_results[13], list_results[14], list_results[15], list_results[16],
                 list_results[17], list_results[18], list_results[19], list_results[20], list_results[21],
                 list_results[22], list_results[23], list_results[24], list_results[25]]))


    if year == 2012:
        list_results = []
        link = f"http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_final_{year}.zip"
        print("Please, wait for data processing! You are downloading a file with 864 mb. This may take a few minutes!")
        response = requests.get(link, stream=True)
        target_path = f'prestacao_final_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        if type_agent == "candidates":
            type_agent = "candidatos"
        if type_agent == "committiees":
            type_agent = "comites"
        if type_data == "revenues":
            type_data = "receitas"
        if type_data == "expends":
            type_data = "despesas"
        df = DataFrame(read_csv(zipfile.ZipFile(f"prestacao_final_{year}.zip", "r").extract(f"{type_data}_{type_agent}_{year}_brasil.txt"), encoding='latin1', sep=';'))
        os.remove(f"prestacao_final_{year}.zip", f"{type_data}_{type_agent}_{year}_brasil.csv")



    if year == 2014:
        link = f"http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_final_{year}.zip"
        print("Please, wait for data processing! You are downloading a file with 864 mb. This may take a few minutes!")
        response = requests.get(link, stream=True)
        target_path = f'prestacao_final_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        if type_agent == "candidates":
            type_agent = "candidatos"
        if type_agent == "committiees":
            type_agent = "comites"
        if type_data == "revenues":
            type_data = "receitas"
        if type_data == "expends":
            type_data = "despesas"
        df = DataFrame(read_csv(zipfile.ZipFile(f"prestacao_final_{year}.zip", "r").extract(f"{type_data}_{type_agent}_{year}_BR.txt"), encoding='latin1', sep=';'))
        os.remove(f"prestacao_final_{year}.zip", f"{type_data}_{type_agent}_{year}_BR.csv")

    if year == 2016:
        link = f"http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_final_2016.zip"
        print("Please, wait for data processing! You are downloading a file with 1 Gb. This may take a few minutes!")
        response = requests.get(link, stream=True)
        target_path = f'prestacao_contas_final_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        if type_agent == "candidates":
            type_agent = "candidatos"
        if type_agent == "committiees":
            type_agent = "comites"
            exit("The committiees accountabilities do not are available in this package version to 2016!")
        if type_data == "revenues":
            type_data = "receitas"
        if type_data == "expends":
            type_data = "despesas"
        df = DataFrame(read_csv(zipfile.ZipFile(f"prestacao_contas_final_{year}.zip", "r").extract(f"{type_data}_{type_agent}_prestacao_contas_final_{year}_brasil.txt"),
                encoding='latin1', sep=';'))
        os.remove(f'prestacao_contas_final_{year}.zip', f"{type_data}_{type_agent}_prestacao_contas_final_{year}_brasil.txt")

    if year == 2018:
        if type_agent == "candidates":
            link = "http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_de_contas_eleitorais_candidatos_2018.zip"
            print(
                "Please, wait for data processing! You are downloading a file with 234 mb. This may take a few minutes!")
            response = requests.get(link, stream=True)
            target_path = f'prestacao_de_contas_eleitorais_candidatos_{year}.zip'
            handle = open(target_path, 'wb')
            for chunk in response.iter_content(chunk_size=512):
                if chunk:
                    handle.write(chunk)
            handle.close()
            if type_data == "revenues":
                df = DataFrame(
                    read_csv(zipfile.ZipFile(f"prestacao_de_contas_eleitorais_candidatos_{year}.zip", "r").extract(
                        f"receitas_candidatos_2018_BRASIL.csv"), encoding='latin1', sep=';'))
            if type_data == "expends":
                print("The data frame will return the contracted expends!")
                df = DataFrame(
                    read_csv(zipfile.ZipFile(f"prestacao_de_contas_eleitorais_candidatos_{year}.zip", "r").extract(
                        f"despesas_contratadas_candidatos_2018_BRASIL.csv"), encoding='latin1', sep=';'))
        if type_data == "committiees":
            exit("The committiees accountabilities do not are available in this package version to 2018!")
    return df





        

