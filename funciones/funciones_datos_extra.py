def frase(nombre, apellido, adjetivo):
          return f'Hola {nombre} {apellido}, eres muy {adjetivo}'

#hay que respetar el orden
frase_resultante = frase('dani','gu','crack')
#si no quieres mantener el orden tienes que hay que declarar cada uno y no importa el orden
segunda_frase_resultante = frase(adjetivo='maquina',apellido='gu',nombre='dani')

print(frase_resultante)
print(segunda_frase_resultante)

#puedo poner un valor por defecto (frase(nombre,apellido,adjetivo='huevon'))
          #frase('dani','gu')
#tambien puedo mover cambiar el valor por defecto
          #frase('dani','gu',adjetivo='malpario')