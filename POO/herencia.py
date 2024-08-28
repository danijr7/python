class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
        def hablar(self):
            print('Hola, estoy hablando un poco.')

""" class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    
    def hablar(self):
        print('Reescribinedo el metodo "hablar".') """

""" class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad """

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f'mi habilidad es {self.habilidad}'

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print(f'hola soy {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')

roberto = EmpleadoArtista('Roberto', 43, 'argentino', 'cantar', 'google', 5000)

herencia1 = issubclass(Artista, Persona)
print(f'-Artista es subclase de Persona: {herencia1}')
herencia2 = issubclass(EmpleadoArtista, Artista)
print(f'-EmpleadoArtista es subclase de Artista: {herencia2}')

instancia = isinstance(roberto, EmpleadoArtista)
print(f'-roberto es una instancia de EmpleadoArtista: {instancia}')