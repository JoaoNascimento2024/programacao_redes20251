porta = int(input("Digite uma porta: "))
# HTTP (80), HTTPS (443), SMTP (25) e SSH (22)
if porta == 80:
    print("HTTP")
elif porta == 443:
    print("HTTPS")
elif porta == 25:
    print("SMTP")
elif porta == 22:
    print("SSH")
else:
    print("Porta desconhecida")
