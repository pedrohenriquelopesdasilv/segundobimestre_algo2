import time

#variaveis globais
ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia):
    global tempo, potencia, ligado
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = nova_potencia
        print(f"Lavadoura de Louças ligada por: {tempo} segundos na potencia {potencia}")
        iniciar_cronometro(tempo)
        desligar() #Desligar no automático
    else:
        print("Maquiná está ligado")
        
def desligar():
    global ligado
    if ligado:
        ligado = False
        print("Máquina está desligado")
    else:
        print("Máquina já está ligado")
        
def status():
    if ligado:
        print(f"Tempo {tempo} segundos /n potencia: {potencia}")
    else:
        print(f"Desligado")
        
def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print(" \nTempo Esgotado")
    
opcao = input("Escolha o Material: vidro(1), plastico(2) e metal(3) :")
def  Vidro():
    ligar(120, 100)
            
def Plastico():
    ligar(60, 21)
    
def Metal():
    ligar(120, 30)
    
if opcao == "1":
    Vidro()
elif opcao == "2":
    Plastico()
elif opcao == "3":
    Metal()