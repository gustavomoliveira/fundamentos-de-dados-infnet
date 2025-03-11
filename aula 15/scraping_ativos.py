from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

#Definindo o browser (Web Driver)
from webdriver_manager.chrome import ChromeDriverManager

#Configurando o browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Abre a janela em modo full screen
driver.maximize_window()
ativo = input("Digite o ativo a ser monitorado: ")

#Acessando a pagina do google
driver.get(f"{ativo}")

#Encontrando o preço
price_element = driver.find_element(By.CLASS_NAME, "js-symbol-last")
print(f'Nome do ativo {ativo} com o preço {price_element.find_element(By.TAG_NAME, "span").text}')

#Fechando o browser
driver.quit()

