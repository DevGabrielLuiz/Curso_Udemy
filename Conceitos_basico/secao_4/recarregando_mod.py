import importlib

import tipos_valores

print(tipos_valores.inteiro)

for i in range(20):
    print (i)
    import tipos_valores
print('fim')

for i in range(20):
    importlib.reload(tipos_valores)
    print (i)

# Modulos sao singleton apenas recarregam uma única vez na memória para garantir performance

# o modulo imporlib com a função reload recarrega o modulo - util caso tenha alguma alteração 
# em runtime


#!! Caso tenha um package

# from _namepack_ .NAMEMOD_ import 'variavel/funca'
