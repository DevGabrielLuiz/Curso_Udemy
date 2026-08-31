#funções que sabem pausar em determina condição

import sys


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() #tem __iter__ e __next__

generator = [n for n in range(10)]
print(generator)
print(iterator)
# generator nao guarda na memoria ele apenas referencia diferente da lista 
# generator nao tem indice nem tamanho e indepente de quantos valores seja
# ele ocupa o mesmo espaço na memoria 
print(sys.getsizeof(generator))
print(next(generator))
# generator gera e pausa a cada execução

def generator(n=0):
    yield 1 # Pausa 
    return 'finish'

gen = generator(0)
