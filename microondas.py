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
        print(f"microondas ligado por: {tempo} segundos na potencia {potencia}")
        iniciar_cronometro(tempo)
        desligar() #Desligar no automático
    else:
        print("Microondas ta ligado")
        
def desligar():
    global ligado
    if ligado:
        ligado = False
        print("Microondas está desligado")
    else:
        print("Microondas já está ligado")
        
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
        
def pipoca():
    ligar(30, 100)
            
pipoca()
#Rodar a função