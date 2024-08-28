cadena1 = 'danigu'
cadena2 = 'el,BaRtO,es,lo,4,mas'
cadena3 = '555565656'

dir = dir(cadena1) #da los atributos
upper = cadena1.upper() #convierte todo a mayusculas
lower = cadena2.lower() #convierte todo a minuscilas
capitalize = cadena2.capitalize() #convierte la primera letra en mayuscula y el resto en minusculas
find = cadena2.find('x') #busca una cadena en otra cadena, si no hay coincidencias devuelve -1 (sino devuelve a partir de donde empieza la primera coincidencia)
index = cadena2.index('e')#busca una cadena en otra cadena (utilizando el elemento completo), si no hay coincidencias lanza una excepcion (sino devuelve a partir de donde empieza la primera coincidencia)
is_numeric = cadena3.isnumeric() #si es numerico devuelve True sino es False
is_alpha_numeric = cadena1.isalpha() #si es alpha numerico ('Aa-Zz' sin espacios) devuelve True sino es False
count = cadena2.count(' ') #cuenta cuantas veces existe un caracter/es de una cadena dentro de otra cadena
len = len(cadena1) #cuenta cuantos caracteres tiene una cadena
startwith = cadena1.startswith('d') #verifica si una cadena empieza con otra cadena dada, si es asi devuelve True
endwith = cadena1.endswith('u') #verifica si una cadena termina con otra cadena dada, si es asi devuelve True
replace = cadena1.replace('u', 'U', 2) #si encuentra una coincidencia la reemplaza por lo dado sino devuelve la cadena anterior y las cantidad de veces que lo quiero realizar
replace2 = cadena1.capitalize()
split = cadena2.split(',') #separar las cadenas con la cadena que le pasemos, convirtiendola en una lista <print(split[3])>

print(split)