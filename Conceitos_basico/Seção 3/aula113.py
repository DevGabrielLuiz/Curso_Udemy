# funções que duplicam quadriplicam e triplicam o valor do parametro
num = float(input('Digite um numero: ')) 
mult = float(input('Digite um numero: ')) 

def dobrar(num):
    elevado = num*2
    return f'O dobro de {num} é: {elevado}'

def triplicar(num):
    elevado = num*3
    return f'O dobro de {num} é: {elevado}'

def quadruplicar(num):
    elevado = num*4
    return f'O dobro de {num} é: {elevado}'
def multiplicar(num,multiplo):
    elevado = num*multiplo
    return f'A multiplicação de {num} por {multiplo} é: {elevado}'

def mult(num):
    def multiplicador(multipli):
        resultado = num*multipli
        return resultado
teste = mult(5)
print(teste(2))
print(dobrar(num))
print(dobrar(num))
print(triplicar(num))
print(quadruplicar(num))
print(multiplicar(num,mult))