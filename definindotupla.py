numero = (5, 8, 12, 8, 7, 8, 3)
#para ser uma tupla precisa estar entre parenteses
print("tupla original: ", numero)
#imprimindo para o usuario a tupla original, sem manipulações
print("Tamanho da tupla: ", len(numero))
print("Acessando indice: ",numero[2])
#escolhendo qual item será mostrado através do indice, lembrando que começa do zero
print("Fazendo um slicing do 2 ao 5", numero[2:5])
#O slicing não pega o ultimo item definido no recorte
print("Quantas vezes o numero 8 repete:", numero.count(8))
print("posição da primeiora ocorrencia do numero 7:", numero.index(7))
minimo_tupla=min(numero)
print("Menor numero dentro da tupla é: ", minimo_tupla)
maximo_tupla=max(numero)
print("Maior numero dentro da tupla é: ", maximo_tupla)
print("soma dos elementos da tupla é: ",sum(numero))
tupla_ordenada=sorted(numero)
print("Os numeros em ordem utilizando o metodo sorted", numero)
print("o numero 4 está na tupla?", 4 in numero)
numero2=(15,20)
tupla_concatenada=numero+numero2
print("A concatenação das tuplas 1 e 2 resulta na nova tupla:", tupla_concatenada)
tupla_duplicada=numero*2
print(tupla_duplicada)