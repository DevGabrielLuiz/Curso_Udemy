import re
import sys
import random
CPF = '746.824.890-70'
lista_para_somar = []
# CPF.replace('.','')\  # um modo mais facil de corrigir os sinais da string
#    .replace('-','')\
#    .replace('.','')
# Outra maneira 
# tudo que não for um número eu substituo por X coisa
# CPF = re.sub(r'[^0-9]','',CPF)

        
entrada_repetida = CPF == CPF[0]*len(CPF)
if entrada_repetida:
        sys.exit()
CPF_semi_corrigido = CPF.split('.')
CPF_corrigido = ''.join(CPF_semi_corrigido)
print(CPF_semi_corrigido)
CPF_corrigido = CPF_corrigido.split('-')
print(CPF_corrigido)
CPF_corrigido = ''.join(CPF_corrigido)
contador_r_digito_1 = 10
contador_r_digito_2 = 11
for _ in range(100):
        for digito in (CPF_corrigido):
           if contador_r_digito_1>=2:
                digito = int(digito)
                lista_para_somar.append(digito*contador_r_digito_1)
                contador_r_digito_1-=1 
print(lista_para_somar)
calc_9_numeros = ((sum(lista_para_somar)*10)%11)
lista_para_somar.clear()
resultado_digito_1 = calc_9_numeros if calc_9_numeros <= 9 else  0 
print(resultado_digito_1)
print(f'CPF corrigido {CPF_corrigido}')


for digito in (CPF_corrigido):
     if contador_r_digito_2>=2:
        digito = int(digito)
        lista_para_somar.append(digito*contador_r_digito_2)
        contador_r_digito_2-=1 
print(f"{lista_para_somar}  = {sum(lista_para_somar)}")
calc_10_numeros = ((sum(lista_para_somar)*10)%11)
print(f"Resultado do calculo do segundo numero: {calc_10_numeros}")
lista_para_somar.clear()
resultado_digito_2 = calc_10_numeros if calc_10_numeros <= 9 else  0 
print(f"Segundo número: {resultado_digito_2}")
primeiros_digitos = str(resultado_digito_1)+str(resultado_digito_2)
cpf_calculado = f'{CPF_corrigido:.9}{primeiros_digitos}'
print(f'CPF calculado = {cpf_calculado:.9} e CPF corrigido = {CPF_corrigido}') 
if cpf_calculado == CPF_corrigido:
        print(f'O CPF {CPF} é válido')
else:
        print(f'O CPF {CPF} é inválido')