class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando.')

nombre = input('Ingresa tu nombre: ')
edad = input('Ingresa tu edad: ')
grado = input('Ingresa tu grado: ')

estudiante1 = Estudiante(nombre,edad,grado)

print(f'''
-Nombre: {estudiante1.nombre}
-Edad: {estudiante1.edad}
-Grado: {estudiante1.grado}
      ''')

while True:
    estudiar = input().lower()
    if estudiar == 'estudiar':
        estudiante1.estudiar()