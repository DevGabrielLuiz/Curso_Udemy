import os
palavra_secreta = 'arroz'
palavra_comparada = f'{'*'*len(palavra_secreta)}'
i=0
print(palavra_comparada)
    
while palavra_secreta!=palavra_comparada:
    
    letra_digitada=input("Digite uma letra:")
    i+=1
    if len(letra_digitada)==1 and letra_digitada.isalpha():
        nova_palavra_comparada = ''
        for posicao_letra in range(len(palavra_comparada)):
            if palavra_secreta[posicao_letra] == letra_digitada:
                nova_palavra_comparada += letra_digitada
            else:
                nova_palavra_comparada += palavra_comparada[posicao_letra]        
        palavra_comparada = nova_palavra_comparada
    else:
        print('DIGITE APENAS UMA LETRA')           
    print(palavra_comparada)
    if palavra_secreta == palavra_comparada:
        os.system('clear')
        break
    print(f'O total de tentativas foi: {i}')
    print(f'Finalmente você acertou !! A palavra era: {palavra_secreta}')
    i=0
