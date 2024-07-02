d1 = {'nome': 'vdfv', 0: 55,'lista':['arroz','pudim']}

if d1.get('z') is None:
    # 'get' ira buscar a chave e se não encontrar ira retornar 'None'
    print('Não existe')
else:
   
    d1.update()
print(d1.keys()) # retorna apenas as chaves podemos armazenar essas chaves uma tupla ou lista
print(d1.values()) # retorna apenas os valores podemos armazenar essas valores uma tupla ou lista
print(list(d1.items())) # retorna a chave e o valor como pares dentro de uma lista dentro de uma tupla. O 'list' é para melhorar a visualização
d1.setdefault('idade',0)
# adiciona valor se a chave não existir
for chave, valor in d1.items():    # 'items' é um iteravel com chave e valor    
    print(chave, valor)
# shallow copy = copia rasa o dicionario apenas copia os valores imutaveis/ em primeiro nivel.  
# Se houver uma altereção em listas ou outros valores mutaveis dentro do dicionario 'd2', elas irão alterar no dicionario inicial 
d2 = d1.copy()    
# d2['lista'][1] = 'feijão'
print(f'Dicionario 1°: {d1}\nDicionario 2°: {d2}')
# ------Para realizar uma cópia profunda devemos import o metodo 'copy' e usar o  d2=copy.deepcopy(d1)
import copy
d2 = copy.deepcopy(d1)    
d2['lista'][1] = 'feijão'
print(f'Dicionario 1°: {d1}\nDicionario 2°: {d2}')
# elimina a chave mas deixa ainda posso acessa-la
nome = d2.pop('nome')
print(nome)
print(d2)
ultima_chave = d1.popitem()  # elimina a ultima chave 
print(ultima_chave)
print(d1)
d1.update({       # cria ou atualiza novos valores
    'nome':'Gabriel',
    'time':'Atlético-MG',
})
d2.update(nome="Gab",cor='pardo') # pode ser feito sendo passado como argumento
tupla = ('altura',1.75), ('Colossenses','1:17')# também funciona com listas
d2.update(tupla) # pode ser feito sendo passado como argumento
