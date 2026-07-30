# split gera uma lista de com a palavras separadas pelo espaço em branco
frase = 'O verbo se fez carne, e habitou entre nós.'
lista_frase = frase.split()
print(lista_frase)
lista_frase = frase.split(',') # ira separar no que eu passar dentro do parenteses
print(lista_frase)
for i,frase in enumerate(lista_frase):
    print(lista_frase[i].strip()) # remove todos os espaços tanto no início quanto no fim 
    # print(lista_frase[i].rstrip) # rstrip remove espaço righit e 
    # print(lista_frase[i].lstrip) # lstrip remove espaço left
    
frases_unidas = '-'.join(lista_frase) # vai concatenar os valores da lista com o separador passado antes do join
print(*lista_frase) # imprime mais bonito