class Humano:
    def __init__(self,edad):
        self.edad = edad
    
    def hablar(self,mensaje):
        print(mensaje)
    
pedro = Humano(75)
raul = Humano(58)

pedro.hablar('-Hola raulito, como estas?')
raul.hablar('-hola pedrito, bien y tu?')
pedro.hablar(f'-Bien gracias, yo tengo {pedro.edad}, y tu?')
raul.hablar(f'-Yo tengo {raul.edad}.')