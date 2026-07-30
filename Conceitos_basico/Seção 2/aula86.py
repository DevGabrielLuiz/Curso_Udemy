lista = ['Maria', 'Judas', "Pedro"]
#lista.append('Tiago')
#indices = range(len(lista))
#for indice in indices:
#    print(indice, lista[indice])
    
lista_enumuerada = enumerate(lista) # desse jeito o python "consome" os valores da lista após ela ser usada, por isso deve se atribuir os valores do enumerate em um outro local.
#print(next(lista_enumuerada)) # ver o primeiro valor + o indice
lista_enumuerada = list(enumerate(lista))
print(lista_enumuerada)
lista_enumuerada = list(enumerate(lista, start=5)) # a lista começa a partir desse valor do start


for indice, item in enumerate(lista_enumuerada[::-1]): # mesma coisa 
    print(indice, item)

for item in lista_enumuerada:
    print(item)