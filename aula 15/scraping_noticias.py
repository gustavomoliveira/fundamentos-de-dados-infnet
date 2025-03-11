import requests
from bs4 import BeautifulSoup

url = ""
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html-parser")
    noticias = soup.find_all("h3")

    for noticia in noticias[:5]: # Exibindo as 5 primeiras manchetes
        print(noticia.text)
else:
    print("Erro ao acessar a página.")