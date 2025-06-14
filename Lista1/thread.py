import threading
import time

def exibirLetras():
    for letra in ["A","B","C","D","E","F","G"]:        
        print(f"Letra: {letra}")
        time.sleep(3.0)
    
def exibirNumeros():
    for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        print(f"Numero: {numero}")
        time.sleep(1.5)  
        
def exibirSimbolos():
    for simbolo in ["#", "!", "$", "%", "*", "@"]:
        print(f"Simbolo: {simbolo}")
        time.sleep(1.5)            

thread1 = threading.Thread(target=exibirLetras)
thread2 = threading.Thread(target=exibirNumeros)
thread3 = threading.Thread(target=exibirSimbolos)

thread1.start()
thread2.start()
thread3.start()

    