#2 listas, una con nombres y otra con apellidos
#escribir los datos en un archivo de texto de forma optima con un for
nombres = ['Zapa','Pelcapo','BigJ','Torito','Barto']
apellidos = ['Bot14','Alejo','Gambuza','Flores','Mitre']

#registrar un txt de forma optima
with open('resolviendo_problemas_resueltos\\nombres_y_apellidos.txt','w') as archivo:
          archivo.write('Los datos son:\n\n')
          for n,a in zip(nombres,apellidos):
                     archivo.writelines(f'Nombre: {n}\nApellido: {a}\n-----------\n')
                     
#en una sola linea
""" [archivo.writelines(f'Nombre: {n}\nApellido: {a}\n-----------\n') for n,a in zip(nombres,apellidos)] """