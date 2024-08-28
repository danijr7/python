class Gato():
    def sonido(self):
        return 'miau'
    
class Perro():
    def sonido(self):
        return 'guau'

def hacer_sonido(animal):
    print(animal.sonido())

cotufa = Gato()
firulais = Perro()

print(cotufa.sonido())
print(firulais.sonido())

hacer_sonido(cotufa)
hacer_sonido(firulais)