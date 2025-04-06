import requests
import os

def definir_arquivo(nome_arquivo, pasta='IBGE'):
    diretorio_corrente = os.path.dirname(__file__)
    caminho_arquivo = os.path.join(diretorio_corrente, pasta, nome_arquivo)
    return caminho_arquivo

def extrair_arquivo(url, caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        print(f'O arquivo já existe em: {caminho_arquivo}.')
        return caminho_arquivo

    try:
        response = requests.get(url)
        response.raise_for_status()
        conteudo = response.content.decode('latin-1')

        with open(caminho_arquivo, 'w', encoding='latin-1') as arquivo:
            arquivo.write(conteudo)

        print(f'O arquivo foi criado com sucesso em: {caminho_arquivo}.')
        return caminho_arquivo
    except Exception as e:
        print(f'Erro ao criar o arquivo: {e}.')
        return None