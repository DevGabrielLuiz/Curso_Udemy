# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
# lista_pergunta = []
# for pergunta in perguntas:
#     lista_opcoes = {}.update(perguntas['Opções']:pergunta.values)
# print(lista_opcoes)
# lista_resposta = []
# for pergunta in perguntas:
#     lista_pergunta.append(pergunta['Pergunta'])
#     lista_opcoes.update({index(pergunta['Opções']) :pergunta['Opções']})
#     lista_resposta.append(pergunta['Resposta'])

    # for indice in perguntas:
    #     print(indice)
    #     if indice =='Pergunta':
    #         lista_pergunta.append(indice)
    #     elif indice =='Opções':
    #         lista_opcoes.append(indice)
    #     elif indice =='Resposta':
    #         lista_resposta.append(indice)
# print(lista_resposta,lista_opcoes,lista_pergunta)

# for pergunta in lista_pergunta:
#     print('Opções')
#     for opcao in lista_opcoes:
#         print(lista_opcoes)
resps = {} 
# resps[cont] = item.values() guardar pode ser importante
contador_acerto=0
for item in perguntas:
    for chave, valor in item.items():
        if chave=='Pergunta':
            print(f'{chave}: {valor}')
        if chave=='Opções':
            cont=1
            for resposta in item['Opções']:
                
                print(f'{cont}){resposta}')
                cont+=1
        if chave=='Resposta':
            Resposta_Usuario=input("Digite a resposta: ")
            if Resposta_Usuario==item['Resposta']:
                print(f'ACERTOU!!!!!')                
                contador_acerto+=1
            else: 
                print(f'ERROU!!!!!')

print(f'Você acertou:{contador_acerto} de {len(perguntas)}')



for pergunta in perguntas:
    print('Pergunta',pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções'] 
    for i, opcao in enumerate(pergunta["Opções"]):
        print(f'{i})', opcao)
    print()
    
    escolha = input('Escolha uma opção: ')
    
    acertou = False    
    escolha_int = None
    qtd_opcoes = len(opcoes)
    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0  and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True  
    
    if acertou:
        contador_acerto+=1
        print('Acertou')
    else:
        print("Errou")
                
print(f'Você acertou:{contador_acerto} de {len(perguntas)}')