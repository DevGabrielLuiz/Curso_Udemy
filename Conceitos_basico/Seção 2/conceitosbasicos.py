#  desempacotamento
lista = ['Maria', 'Judas', "Pedro"]

nome1, nome2, nome3 = lista
name1, *resto = lista  # Atribui os valores que sobram do empacotamento a variavel situada após o '*'
print(resto)
# empacotamento