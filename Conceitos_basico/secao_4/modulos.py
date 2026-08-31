#import, froom as e *

# inteiro - import - nome modulo
# vantagem voce tem o namespace do modulo (ter variaveis com mesmo nome do modulo)
# desvantagem: nome grande 

from sys import exit as sair

sair()
print('saiu')

# oartes -from nome_moduulo import objeto
#vantagem: nome pequeno 
#desvantagem : sem namespace 

# alias 1 - import nome_modulo as apelido 
# alias 2 - from nome_modulo import objeto as apelido
# Vantagem: você pode reservar nomes para seu código
# desvantagem: pode ficar fora do padrão da linguagem 

# má prática - from nome_modulo import *
# vantagens :importa tudo de um módulo
# desvantagem: importa tudo de um módulo