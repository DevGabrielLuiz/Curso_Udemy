# São dados mutáveis mas que aceitam apenas dados imutáveis
# set(iterável) ou {1,2,3}
# O método SET não garante a ordem e não possui index


s1 = set('Gabriel') # ele passa de maneira iterada
s2 = {'Gabriel', 1.2, 3}
# s3 = {'Gabriel', 1.2, [1,2,3]} # ira retornar erro de tipagem
s4 = {'Gabriel', 1.2, (1,2,3,3)} # ira ser aceito
# print(s1[1]) # ira retornar erro 
# Seus valores serão sempre únicos ou 
# s5 = {'Gabriel', 1.2, {"1":1,"2":2,"3":4}} # não ira ser aceito
# s6 = {'Gabriel', 1.2, (1,2,3,3,3,3,3,3,5,"azul"), } # ira ser aceito
# print(s6)
# for item in s2:
#     print(item)

# Métodos úteis:
# add, clear, update, discard

# s2.add('Luiz')
# print(s2)
# s4.update('Luiz') # adiciona de maneira iterável 
# print(s4)
# s1.clear() # Limpa o set 
# s2.discard('Luiz') #elimina apenas o elemento passado e não apresenta erro caso não tenha o elemento
# s2.remove('Luiz') # apresenta erro caso não tenha o elemento
# print(s2)

# Operadores úteis 
# uniao | uniao (union) -> Une
# interseção & (intersection) -> Itens presentes em ambos 
# diferença - ->Itens presentes apenas no set da esquerda 
# diferença simetrica ^ -> Itens que não estão em ambos 
teste1 = {1, 2, 3}
teste2 = {2, 3, 4}
# union
# testUNION = teste1 | teste2  #Ambos os jeitos fucionam
# testUNION = teste1.union(teste2)
# print(testUNION)

# Interserção
# testIntersection = teste1 & teste2  #Ambos os jeitos fucionam
# testIntersection = teste1.intersection(teste2)
# print(testIntersection)

# Diferença 
testDiference = teste1 - teste2  #Ambos os jeitos fucionam
testDiference = teste1.difference(teste2)
print(testDiference)

# Diferença simetrica
testDiference = teste1 ^ teste2  #Ambos os jeitos fucionam
testDiference = teste1.symmetric_difference(teste2)
print(testDiference)
# Diferença 
testegeral = teste1.issuperset(teste2)
print(testegeral)