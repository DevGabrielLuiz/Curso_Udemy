lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2),
    {0, 1}, {'nome': 'Luiz'}, 
]
# isinstance('objeto a ser analisado', 'instancia que eu quero saber')
# serve para verificar se um objeto pertence a aquela instância especifica.
for item in lista:
    print(item, isinstance(item, tuple))