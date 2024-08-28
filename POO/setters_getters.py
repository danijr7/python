class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    #con un getter accedo a la funcion mediante un def
    def get_nombre(self):
        return self.__nombre
    
    #con un setter cambio el valor de la funcion
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

dani = Persona('dani', 19)
nombre = dani.get_nombre()
print(nombre) #nombre = "dani"

dani.set_nombre('kike')
nombre = dani.get_nombre()
print(nombre) #