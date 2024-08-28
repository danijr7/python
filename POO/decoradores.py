def decorador(funcion):
    def fun_mod():
        print('Antes de llamar a la funcion')
        #decorador y lo puedo poner en donde sea
        funcion()
        print('Desp de llamar a la funcion')
    return fun_mod

""" def saludo():
    print('alo dani')

#le asigno una variable para convertirla en una funcion
saludo_mod = decorador(saludo)
saludo_mod() """

#funcion q le pasamos a la 1ra funcion, resume lo q esta comentado
@decorador
def saludo():
    print('ola chavales')

saludo()