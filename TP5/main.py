import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from bd_mysql import *

def fazer_requisicao(url, fonte='ibge'):
    try:
        resposta = requests.get(url)
        
        if resposta.status_code != 200:
            mensagem_erro = f'Erro HTTP: código {resposta.status_code}'
            
            if fonte == 'bbc':
                registrar_erro_bbc(mensagem_erro, url)
            else:
                registrar_erro_ibge(mensagem_erro, url)
                
            return None, {
                'url': url,
                'status_code': resposta.status_code,
                'data_acesso': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'content_type': None,
                'content_length': None
            }
        
        metadados = {
            'url': url,
            'status_code': resposta.status_code,
            'data_acesso': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'content_type': resposta.headers.get('Content-Type'),
            'content_length': resposta.headers.get('Content-Length')
        }
        
        return resposta, metadados
    
    except Exception as erro:
        mensagem_erro = f'Erro na requisição: {erro}'
        
        if fonte == 'bbc':
            registrar_erro_bbc(mensagem_erro, url)
        else:
            registrar_erro_ibge(mensagem_erro, url)
            
        return None, {'url': url, 'data_acesso': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

def extrair_dados_ibge(url):
    resposta, metadados = fazer_requisicao(url, fonte='ibge')
    
    if resposta is None:
        registrar_erro_ibge('URL não acessível', url)
        return pd.DataFrame(), metadados
    
    try:
        conteudo = resposta.content.decode('latin-1')
        linhas = conteudo.splitlines()
        dados = []
        
        for linha in linhas:
            linha = linha.strip()
            
            if linha.isupper() or linha == '':
                continue
            
            linha_normalizada = linha.replace('\x96', '-').split(' - ')
            if len(linha_normalizada) >= 3:
                dados.append({
                    'serial': linha_normalizada[0],
                    'descritivo': linha_normalizada[1],
                    'ano': linha_normalizada[2]
                })
        
        if not dados:
            registrar_erro_ibge('Nenhum dado encontrado', url)
            
        df_dados = pd.DataFrame(dados)
        return df_dados, metadados
    
    except Exception as erro:
        registrar_erro_ibge(f'Erro ao processar dados: {erro}', url)
        return pd.DataFrame(), metadados

def extrair_noticias_bbc(url):
    resposta, metadados = fazer_requisicao(url, fonte='bbc')
    
    if resposta is None:
        registrar_erro_bbc('URL não acessível', url)
        return pd.DataFrame(), metadados
    
    try:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        noticias = []
        
        for h3 in soup.find_all('h3'):
            link_tag = h3.find('a')
            if link_tag and link_tag.get_text(strip=True):
                titulo = link_tag.get_text(strip=True)
                link = link_tag.get('href')
                
                termos_ignorar = ['WhatsApp', 'Facebook', 'YouTube', 'TikTok', 'Instagram', 'X', 
                                 'Parceiros comerciais da BBC Brasil', 'Twitter']
                
                if titulo in termos_ignorar:
                    continue
                
                if link and not link.startswith('http'):
                    link = f"https://www.bbc.com{link}"
                
                noticias.append({
                    'titulo': titulo,
                    'link': link,
                    'data_extracao': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
        
        if not noticias:
            registrar_erro_bbc('Nenhuma notícia encontrada', url)
            
        df_noticias = pd.DataFrame(noticias)
        return df_noticias, metadados
    
    except Exception as erro:
        registrar_erro_bbc(f'Erro ao processar dados: {erro}', url)
        return pd.DataFrame(), metadados

if __name__ == '__main__':
    criar_tabela("""
        CREATE TABLE IF NOT EXISTS tp5_pb.erros_ibge (
            id INT AUTO_INCREMENT PRIMARY KEY,
            url_acessada VARCHAR(255),
            erro TEXT,
            data_erro DATETIME
        )
    """)
    
    criar_tabela("""
        CREATE TABLE IF NOT EXISTS tp5_pb.erros_bbc (
            id INT AUTO_INCREMENT PRIMARY KEY,
            url_acessada VARCHAR(255),
            erro TEXT,
            data_erro DATETIME
        )
    """)

    URL_IBGE = 'https://ftp.ibge.gov.br/Acesso_a_internet_e_posse_celular/2015/Tabelas_de_Resultados/indice_de_tabelas.txt'
    df_ibge, metadados_ibge = extrair_dados_ibge(URL_IBGE)

    if not df_ibge.empty:
        criar_tabela("""
            CREATE TABLE IF NOT EXISTS tp5_pb.tabela_ibge (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url_acessada VARCHAR(255),
                data_acesso DATETIME,
                serial VARCHAR(255),
                descritivo TEXT,
                ano VARCHAR(10)
            )
        """)

        if tabela_esta_vazia('tp5_pb.tabela_ibge'):
            salvar_dados_ibge(df_ibge, URL_IBGE)
        else:
            print("A tabela do IBGE já contém dados. Nenhum dado será inserido.")

        criar_tabela("""
            CREATE TABLE IF NOT EXISTS tp5_pb.metadados_ibge (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url_acessada VARCHAR(255),
                status_code INT,
                data_acesso DATETIME,
                content_type VARCHAR(100),
                content_length VARCHAR(100)
            )
        """)
        
        salvar_metadados_ibge(metadados_ibge)
    else:
        print("Não foi possível obter dados do IBGE.")

    URL_BBC = 'https://www.bbc.com/portuguese'
    df_bbc, metadados_bbc = extrair_noticias_bbc(URL_BBC)

    if not df_bbc.empty:
        criar_tabela("""
            CREATE TABLE IF NOT EXISTS tp5_pb.noticias_bbc (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url_acessada VARCHAR(255),
                data_acesso DATETIME,
                titulo TEXT,
                link VARCHAR(255)
            )
        """)

        if tabela_esta_vazia('tp5_pb.noticias_bbc'):
            salvar_noticias_bbc(df_bbc, URL_BBC)
        else:
            print("A tabela de notícias da BBC já contém dados. Nenhuma notícia será inserida.")
            
        criar_tabela("""
            CREATE TABLE IF NOT EXISTS tp5_pb.metadados_bbc (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url_acessada VARCHAR(255),
                status_code INT,
                data_acesso DATETIME,
                content_type VARCHAR(100),
                content_length VARCHAR(100)
            )
        """)
        
        salvar_metadados_bbc(metadados_bbc)
    else:
        print("Não foi possível obter notícias da BBC.")