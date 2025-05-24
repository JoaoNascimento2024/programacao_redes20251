import requests

site = input("Digite o nome de um site: ")
conteudo = requests.get(site)

with open("index.html","w", encoding = conteudo.apparent_encoding) as arquivo:
    arquivo.write(conteudo.text)
    arquivo.close()