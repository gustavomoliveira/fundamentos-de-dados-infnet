import requests
from bs4 import BeautifulSoup
import os, pandas as pd
from conectar_db import conectar_mysql
from arquivo import *

URL = 'https://ftp.ibge.gov.br/Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/indice_de_tabelas.txt'
    
def separar_linhas(arquivo_ibge):
    try:
        with open(arquivo_ibge, 'r', encoding='latin-1') as arquivo:
            linhas = arquivo.readlines()
        return linhas
    except Exception as e:
        print(f'Erro ao separar as linhas: {e}.')
        return []
    
def scraping_ibge(url):
    caminho_arquivo = definir_arquivo('indice_de_tabelas.txt')
    arquivo_ibge = extrair_arquivo(url, caminho_arquivo)
    linhas = separar_linhas(arquivo_ibge)

    dados_tabela = []

    for linha in linhas:
        linha = linha.strip()

        if linha.isupper() or linha == '':
            continue
        
        if ' - ' in linha:
            partes = linha.split(' - ')
            serial = partes[0]
            restante = partes[1].split('  ')
            descritivo = restante[0]
            print(descritivo)
            ano = restante[1]
        else:
            partes = linha.split('  ')
            serial = partes[0]
            descritivo = ' '.join(partes[1:-1])
            ano = partes[-1]

        dados_tabela.append({
            'serial': serial,
            'descritivo': descritivo,
            'ano': ano
        })

    df_ibge = pd.DataFrame(dados_tabela)
    print(df_ibge)
        
scraping_ibge(URL)



        


