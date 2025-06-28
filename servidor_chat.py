import socket
import threading

#Armazena os clientes conectados
clientes = []

def iniciar_servidor():
    #Cria objeto socket para funcionar com IPV4 e TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Vincula endereço e porta para esperar conexões
    servidor.bind(("0.0.0.0",5000))
    #Inicializa o servidor. Agora ele fica ouvindo conexões
    servidor.listen()
    print("Servidor inicializado!!!")

    while True:
        #Captura cliente que abriu conexão
        cliente, endereco = servidor.accept()        
        clientes.append(cliente)
        thread = threading.Thread(target = tratar_mensagens_cliente, args=(cliente, endereco))
        thread.start()

def tratar_mensagens_cliente(cliente, endereco):
    while True:
        try:
            mensagem = cliente.recv(5000)
            print(mensagem.decode())
            if mensagem:
                enviar_mensagens_clientes(mensagem, cliente)
        except:
            break
    cliente.close()
    clientes.remove(cliente)
    print(f"{endereco} foi desconectado!!!")

def enviar_mensagens_clientes(mensagem, cliente):
    for cliente_for in clientes:
        if cliente != cliente_for:
            try:
                cliente_for.send(mensagem)
            except:
                cliente_for.close()
                clientes.remove(cliente_for)

iniciar_servidor()