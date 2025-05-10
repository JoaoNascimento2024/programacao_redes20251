def validarIP(ip):
    if "192.168.1." in ip:
        numerosIP = ip.split(".")    
        numeroFinal = int(numerosIP[3])
        if numeroFinal > 0 and numeroFinal < 256:
            return True
        else:
            return False
    else:
        return False


ips = []
while True:
    ip = input("Digite o IP: ")
    if ip.lower() == "fim":
        break
    if validarIP(ip):
        ips.append(ip)

for ip in ips:
    print(ip)

for i in range(1,11):
    if i == 4:
        break
    print(i)
