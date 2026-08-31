# dir, hasattr e getattr
# visualzar no 'debug console os metodos e atributos de determinada string 
# dir mostra todos os metodos que eu posso executar nessa string 
# hasattr verifica se o metodo existe para aquela string
# getattr pega o metodo dinamicamente 


texto = 'GAbriel'
metodo = 'lower'
if hasattr(texto, 'upper'):
   print(texto.upper)
   print(getattr(texto, metodo)())
    
