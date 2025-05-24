arquivo = open("./lista1/q5.py","r")
linhas = arquivo.readlines()
#print(len(linhas))
for linha in linhas:
    print(linha)
arquivo.close()
