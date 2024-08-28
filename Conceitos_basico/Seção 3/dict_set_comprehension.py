
from hashlib import shake_128


produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5, 
    'categoria': "Escritório",
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor 
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

print(dict(lista))
# a funcao "dict aceita listas que se 'parecem com dicionarios' "

dc = {
    chave: valor
    for chave, valor in lista
}

s1= {i + i*2 for i in range(10)}
print(s1)