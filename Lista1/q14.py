import os

diretorio = "c:\\temp"

arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    nome_atual = f"{diretorio}\\{arquivo}"
    novo_nome = f"{diretorio}\\novo_{arquivo}"
    os.rename(nome_atual, novo_nome)



