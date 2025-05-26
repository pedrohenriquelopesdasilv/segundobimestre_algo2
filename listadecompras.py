lista_compras = []
while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Finalizar")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        item = input("Digite o nome do item a ser adicionado: ")
        lista_compras.append(item)
        print(f"'{item}' foi adicionado à lista.")

    elif opcao == "2":
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' foi removido da lista.")
        else:
            print(f"'{item}' não está na lista.")

    elif opcao == "3":
        if lista_compras:
            print("\nItens na sua lista de compras:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
        else:
            print("Sua lista de compras está vazia.")

    elif opcao == "4":
        print("Finalizando a lista de compras.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1 a 4).")

print("\nLista final de compras:")
for i, item in enumerate(lista_compras, 1):
    print(f"{i}. {item}")