class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'My name is: {self.nombre} and I am {self.edad}.'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)

humano1 = Persona('dani',19)
humano2 = Persona('pepo',10)
humano3 = Persona('juana',9)
#print(humano1)

""" repre = repr(humano1)
resultado = eval(repre) """

nueva_persona = humano1 + humano2 + humano3
print(nueva_persona.edad)