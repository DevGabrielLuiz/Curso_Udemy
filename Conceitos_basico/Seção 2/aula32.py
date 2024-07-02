"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")
try:
  if numero.isdigit():
#   if numero % 2 == 0:
      print(f"O número {numero} é par")
  else:
      print(f'O número {numero} é ímpar')
except:
  print('Você não digitou um número inteiro.')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora=int(input("Digite a hora"))
    if hora>=0 and hora<=11:
        print('Bom dia ')
    elif hora>11 and hora<=12:
        print('Boa tarde')
    elif hora>18 and hora<=23:
        print('Boa noite')
except:
    print('Hora inválida')




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Por favor, digite seu nome: ")

if nome.isalpha(): #verifica se nnome é um digito
  try:
    if len(nome) <= 4:
      print("Seu nome é curto")
    elif len(nome) <= 6:
      print("Seu nome é normal")
    else:
      print("Seu nome é grande")
  except:
    print("Você não escreveu uma palavra")
else:
  print("Você digitou um nome inválido")
