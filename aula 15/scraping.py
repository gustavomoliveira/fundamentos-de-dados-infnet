import requests
from bs4 import BeautifulSoup

url = ""  # Substitua pelo link do produto desejado
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    preco = soup.find("b", class_="regularPrice")
    if preco:
        print(f"Preço do produto: {preco.text}")
    else:
        print("Preço não encontrado.")
else:
    print("Erro ao acessar a página.")

