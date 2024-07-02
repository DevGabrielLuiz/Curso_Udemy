import os

lista_compras = []
# lista_compras = list(enumerate(lista_compras))

# indices  = range(len(lista_compras))
while True:
    print('Selecione uma opção')
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system('cls')
        valor =input("Valor: ")
        lista_compras.append(valor)
    elif opcao == 'a':  
        
        indice_remover=int(input("Qual indice deseja apagar: "))  
        try:
            del lista_compras[indice_remover]
        except:
            print("Indice inválido")
    elif opcao == 'l':
            os.system('cls')
            if len(lista_compras) == 0:
                print('Nada para listar')
            for i,valor in enumerate(lista_compras):
                print(i, valor)
    elif opcao=='close':
        break
    else:
        print("Digite uma opção válida")