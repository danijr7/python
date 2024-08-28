#para cuando la carpeta esta en la misma ruta
#import funciones_buenas.saludar as saludando

#se utliza para importar modulos de otras rutas
import sys

#importo el archicho en otra ruta
sys.path.append('C:\\Users\\kike\\Desktop\\Curso de Python\\funciones_buenas')

#luego importo el modulo normalmente
import saludar

#puedo utilizarlo normalmente
print(saludar.saludar('ELbicho'))