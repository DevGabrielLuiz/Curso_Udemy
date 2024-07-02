frase = 'O Python é uma linguagem de programação '\
    'multiparadigma.'\
    'Python foi criada por Guido van Rossum'
i = 0
letra = ''
letra_count = 0
while i<len(frase):
    if frase[i]==' ':
        i+=1
        continue
    if letra_count<=frase.count(frase[i]) :
        letra=frase[i]
        letra_count=frase.count(frase[i])
    i+=1
print(f'A letra {letra} aparece {letra_count} vezes!')