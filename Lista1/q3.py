ip = input("Digite o número IP: ")
if "192.168.1." in ip:
    numerosIP = ip.split(".")    
    numeroFinal = int(numerosIP[3])
    if numeroFinal > 0 and numeroFinal < 256:
        print("IP válido")
    else:
        print("IP inválido")    
else:
    print("IP inválido")