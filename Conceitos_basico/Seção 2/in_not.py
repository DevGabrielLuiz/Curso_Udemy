# Operadores in e not in 
# o in vai em item por item
# Strings são iteráveis 
# 0 1 2 3 4 5
# o t a v i o
#-6-5-4-3-2-1
# nome = "otávio"
# print(nome[2])
# print(nome[-4])
# print('á' in nome)
# print('z' not in nome)

nome= input("Digite o nome:")
idade= input("Digite a sua idade:")
if nome and idade:
    print("Você deixou campos vazios!")
    
else:
    print(f'Seu nome é: {nome} e sua idade é {idade}')    
    print(f'Seu nome invertido é: {nome[::-1]} ')
    
    if " " not in nome:
        print(f'Seu nome não contém espacos. ')
    else:
        print(f'Seu nome contém espacos. ')
        
    print(f'Seu nome tem {len(nome)} letras ')
    print(f'A primeira letra é {nome[0]}')
    print(f'A última letra é {nome[-1]}')
    