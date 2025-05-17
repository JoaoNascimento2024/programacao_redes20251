
import requests
from bs4 import BeautifulSoup

url = "https://rntv.com.br/"

resposta = requests.get(url)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, "html.parser")
    manchetes = soup.find_all("h3")

    print("Manchetes principais: ")
    for noticia in manchetes:
        print(noticia.text)