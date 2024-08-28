#importo el modulo con su nombre (las funciones de otros modulos se convierten en metodos)
import modulo_saludar as nombre_prop #le puede poner un nombre mas facil de manejar

#inicializo una variable en la que accedemos a la funcion (como metodo) mediante el nameSpace (modulo_saludar)
saludo = nombre_prop.saludar('messi')
print(saludo)

#--------------------------------------------------------------------

#para importar una funcion/es especifica de otro modulo
from modulo_saludar import saludar as saludar_como_persona,saludar_raro as saludar_como_facho #puedo renombrar la funcion

#en este caso se puede utilizar como una funcion
saludo = saludar_como_persona('ronaldo')
print(saludo)

saludo = saludar_como_facho('cfk')
print(saludo)

#-------------------------------------------------------------------------

#para importar todo de otro modulo (puede no ser la mejor opcion pq el modulo importado puede ser muy pesado)
from modulo_saludar import *

#en este caso se puede utilizar como una funcion
saludo = saludar('ronaldo')
print(saludo)

saludo = saludar_raro('cfk')
print(saludo)

#para ver todas las propiedades y metodos del nameSpace
#print(dir(nombre_del_nameSpace))