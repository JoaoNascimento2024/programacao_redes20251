latencias = []
while True:
    latencia = input("Latência: ")
    if latencia == "-1":
        break
    latencias.append(float(latencia))

print("A menor latência é: " + str(min(latencias)))
print("A maior latência é: " + str(max(latencias)))
print("A média latência é: " + str(sum(latencias) / len(latencias)))

