from abc import ABC, abstractmethod

class Trabajador(ABC):  
    @abstractmethod
    def trabajar(self):
        pass

class Comedor:
    @abstractmethod
    def comer(self):
        pass

class Durmiente:
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador,Comedor,Durmiente):
    def comer(self):
        print('el humano esta comiendo')
    
    def trabajar(self):
        print('el humano esta trabajando')
    
    def dormir(self):
        print('el humano esta durmiendo')

class Robot(Trabajador):
    
    def trabajar(self):
        print('el humano esta trabajando')\

robot = Robot()
humano = Humano()

robot.trabajar()
humano.comer()
humano.trabajar()
humano.dormir()