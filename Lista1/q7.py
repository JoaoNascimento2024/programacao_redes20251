numeroSwitches = int(input("Digite o número de switchs da rede: "))

switchs = []
for i in range(numeroSwitches):
    portas = int(input("Número de portas do switch " + str(i+1) + "? "))
    switchs.append(portas)

for switch in switchs:
    print("Número de portas: " + str(switch))  
