import requests
import pandas as pd
import matplotlib.pyplot as plt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#Definindo o browser (Web Driver)
from webdriver_manager.chrome import ChromeDriverManager

import time
from io import BytesIO

def obter_dados_seguranca_publica(url):

    #Detecta a instalação e verifica se na instalação do chrome local tem o web driver
    service = Service(ChromeDriverManager().install())

    #Utilizando o driver local para o chrome https://googlechromelabs.github.io/chrome-for-testing/
    #path = "D:\\source\\ProjetoBlocoFundamentosDados\\web-scraping\\chromedriver.exe"
    #service = Service(executable_path=path)

    #Configurando o browser
    driver = webdriver.Chrome(service=service)

    #Abre a janela em modo full screen
    driver.maximize_window()

    #Acessando a pagina do google
    driver.get(url)

    links = driver.find_elements(By.CLASS_NAME, "dataset-heading")

    for link in links:
        if (link.text == "Informações Institucionais de Segurança Pública"):
            #Navegando para a proxima pagina
            driver.get(link.find_element(By.TAG_NAME, "a").get_attribute("href"))
            break

    #Esperando a pagina a carregar
    time.sleep(1)

    #Obtendos novos links
    links = driver.find_elements(By.CLASS_NAME, "heading")


    for link in links:
        if (link.text.startswith("UPP: datas de ocupação")):
            driver.get(link.get_attribute("href"))
            break

    #Esperando a pagina a carregar
    time.sleep(1)
    
    link_dados_arquivo = ''
    table_rows = driver.find_elements(By.TAG_NAME, "tr")
    for tr in table_rows:
        if (tr.text.startswith("Link de acesso ao recurso")):
            link_dados_arquivo = tr.find_element(By.TAG_NAME, "td").find_element(By.TAG_NAME, "a").text
    
    return link_dados_arquivo

def ler_arquivo_seguranca(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if (response.status_code != 200):
        print(f'Erro ao acessar a pagina: {response.status_code}') 
        return None
    
    #Metadados da resposta do servidor 
    for key in response.headers.keys():
        print(f'{key}: {response.headers[key]}')
    
    #Pega a resposta e ler no data frame
    data = pd.read_excel(BytesIO(response.content))

    return data


if __name__ == "__main__":
    url = "https://dadosabertos.rj.gov.br/dataset/?organization=isp"    
    url_arquivo_dados = obter_dados_seguranca_publica(url)

    #Pega a resposta do servidor e cria um data frame
    dataframe = ler_arquivo_seguranca(url_arquivo_dados)

    #Dados obtidos pela site de segurança
    print(dataframe.head())