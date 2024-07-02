
def mult(*args):
    result_args = 1
    
    for valor in args:
        
        result_args*=valor
        print(result_args)
    print(result_args)
    return result_args

print(mult(2,4))

#  2 exercicio

def par_impar(val):
    if val%2==0:
        return 'PAR'
    return 'IMPAR'

print(par_impar(0))