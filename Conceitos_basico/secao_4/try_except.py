# Try, except, else e finally

try:
    ...
    
except:
    ...
#O ideal é eu passar o nome do erro
# caso eu não faça isso Exception vai tratar qulaquer erro não resolvido.

try:
    10/0
    
    ...
    
except ZeroDivisionError as e:
    print(e.__class__.__name__, "imprime o erro que foi dado")
except (TypeError, ZeroDivisionError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome', error.__class__.__name__)
except Exception: 
    print('Erro desconhecido')

else:
    print('execytadi quando não tem erro')
finally: 
    
    print('Finally sempre é executado mesmo com erro')
