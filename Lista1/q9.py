"""
Peça ao usuário o endereço MAC de um dispositivo e verifique se o endereço
começa com &quot;00:1A:2B&quot;, indicando que pertence a um determinado fabricante.
Caso contrário, informe que é de outro fabricante.
"""

mac = input("Digite um endereço MAC de um dispositivo: ")
if mac.startswith("00:1A:2B"):
    print("Pertence ao fabricante")
else:
    print("Não pertence")
    