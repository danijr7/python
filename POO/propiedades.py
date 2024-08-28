class Persona:
    # Método constructor: se ejecuta cuando se crea una nueva instancia de la clase Persona.
    def __init__(self, nombre, edad):
        # Atributo privado (por convención) que almacena el nombre.
        self.__nombre = nombre
        # Atributo público que almacena la edad.
        self.edad = edad
    
    # Propiedad: permite acceder al atributo privado __nombre como si fuera público.
    @property
    def nombre(self):
        return self.__nombre
    
    # Setter: permite modificar el valor del atributo privado __nombre.
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    # Deleter: permite eliminar el atributo privado __nombre.
    @nombre.deleter
    def nombre(self):
        del self.__nombre 

# Creación de una instancia de la clase Persona con nombre 'dani' y edad 19.
dani = Persona('dani', 19)

# Acceso al atributo nombre a través de la propiedad.
nombre = dani.nombre
print(nombre)  # Imprime: dani

# Modificación del atributo nombre a través del setter.
dani.nombre = 'kike'

# Acceso nuevamente al atributo nombre después de la modificación.
nombre = dani.nombre
print(nombre)  # Imprime: kike
