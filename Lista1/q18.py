import os

diretorio = "c:\\temp"
arquivos = os.listdir(diretorio)

contador = 0
arquivosErro = []
for arquivo in arquivos:
    if ".log" in arquivo:
        file = open(f"{diretorio}\\{arquivo}","r")
        possuiErro = False
        linhasErros = []
        i = 1
        for linha in file.readlines():            
            if "ERROR" in linha:
                possuiErro = True
                contador = contador + 1
                linhasErros.append(i)
            i = i + 1
        if possuiErro:
            for linha in linhasErros:
                arquivosErro.append({"arquivo" : arquivo, "linha" : linha})
        file.close()

print("Número de erros: " + str(contador))
print(arquivosErro)

for arquivo in arquivosErro:
    nomeArquivo = arquivo["arquivo"]
    linha = arquivo["linha"]
    print(f"arquivo[{nomeArquivo}] = Linha: {linha}")