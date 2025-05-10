velocidade = int(input("Velocidade de download (Mbps): "))
if velocidade < 10:
    print("Valocidade baixa!")
if velocidade >= 10 and velocidade <= 100:
    print("Velocidade normal!")
else:
    print("Velocidade alta!")


