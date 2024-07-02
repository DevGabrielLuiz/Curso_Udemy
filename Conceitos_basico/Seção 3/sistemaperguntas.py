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
lista_pergunta = []
lista_opcoes = {}
lista_resposta = []
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
for item in perguntas:
    for chave, valor in item.items():
        print(chave,valor)
        if chave=='Opções':
            print(f'{valor}\n')
        if chave=='Resposta':
            continue
        
        # print(Opcoes)
    