from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractmethod
    def hacer_act(self):
        pass
    
    def presentarse(self):
        print(f'hola, me llamo {self.nombre} y tengo {self.edad} de edad.')

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_act(self):
        print(f'Estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_act(self):
        print(f'Estoy trabajando de: {self.actividad}')



carlitos = Estudiante('carlos', 16, 'masculino', 'medicina')
dieguito = Trabajador('diego', 9, 'masculino', 'futbolista')

carlitos.presentarse()
carlitos.hacer_act()
dieguito.presentarse()
dieguito.hacer_act()