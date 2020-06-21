def voters(year = None):
    from pandas import DataFrame, read_csv, concat
    from sys import exit
    import requests, zipfile, os

    link = f"http://agencia.tse.jus.br/estatistica/sead/odsele/perfil_eleitorado/perfil_eleitorado_{year}.zip"
    nomes_perfil_el = ['PERIODO', 'UF', 'MUNICIPIO', 'COD_MUNICIPIO_TSE', 'NR_ZONA', 'SEXO', 'FAIXA_ETARIA',
                          'GRAU_DE_ESCOLARIDADE', 'QTD_ELEITORES_NO_PERFIL']
    list_results = list()

    if year not in list(range(2004, 2019, 2)):
        exit("Pleace, choose a valid year!")
    else:
        print("Please, wait for data processing!")
        response = requests.get(link, stream=True)
        target_path = f'perfil_eleitorado_{year}.zip'
        handle = open(target_path, 'wb')
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)
        handle.close()
        df = DataFrame(read_csv(zipfile.ZipFile(f"perfil_eleitorado_{year}.zip", "r").extract(f"perfil_eleitorado_{year}.txt"),
                         encoding='latin1', sep=';', names= nomes_perfil_el))
        os.remove(f"perfil_eleitorado_{year}.zip", "LEIAME.pdf", f"perfil_eleitorado_{year}.txt")
        return df
