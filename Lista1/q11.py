import os

pasta = r"C:\Users\1724026\Desktop\programacao_redes20251\Lista1"

conteudoArquivos = os.listdir(pasta)

for arquivo in conteudoArquivos:
    print(arquivo)