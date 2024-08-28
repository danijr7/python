#1 profesor (el de mayor edad)
#1 asistente (el de menor edad)
#pedir la edad y nombre de todos los alumnos de la clase
#mostrar quien es el alumno y quien el asistente

cant_alumnos = int(input('Ingrese la cantidad de alumnos: '))

def obtener_alumno(cant_alumnos): #creando la funcion para los alumnos
          #creando la lista de alumnos
          alumno = []
          #ejecutando el bucle para pedir nombre y edad de cada alumno
          for i in range(cant_alumnos):
                    edad = int(input('Ingrese la edad del alumno: '))
                    nombre = input('Ingrese el nombre del alumno: ')
                    alumno = (edad,nombre)
                    #agregando cada nombre y edad
                    alumno.append(alumno)
          #ordenando de mayor a menos por la edad
          alumno.sort(key=lambda x : x[1])
          #alumno[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y al profesor
          assistente = alumno[0][0]
          profesor = alumno[-1][0]
          #retornamos la tupla
          return assistente,profesor
#desenpaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_alumno(3)

print(f'el profesor es : {profesor} y su asistentes es: {asistente}')