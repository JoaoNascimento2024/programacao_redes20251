import requests
path = "https://conteudo.imguol.com.br/c/noticias/35/2024/04/03/onca-pintada-atacando-jacare-no-pantanal-e-uma-das-imagens-vencedoras-do-premio-sony-award-photography-1712152555836_v2_900x506.jpg.webp"
conteudo = requests.get(path)
arquivo = open("imagem.webp","bw")
arquivo.write(conteudo.content)
arquivo.close()