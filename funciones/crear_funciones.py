#creando una fuincion simple

""" def saludar():
          print('Hola q tal chavales')
          
saludar() """

def saludar(nombre,sexo):
          sexo = sexo.lower()
          if sexo=='mujer':
                    print(f'hola {nombre}, como estas tia')
          elif sexo=='hombre':
                    print(f'hola {nombre}, como estas chaval')
          else:
                    print(f'hola {nombre}, como estas carck')
          
#saludar('tony','Hombre')

#crear una funcion que retorne valores
def crear_clave(num):
          chars = 'abcdefghij'
          num_entero = str(num)
          num = int(num_entero[0])
          c1 = num - 2
          c2 = num
          c3 = - 5
          clave = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
          return clave,num #se queda el valor final para manejarlo despues

password,primer_numero = crear_clave(3)

print(f'Tu clave nueva es: {password}')
print(f'El numero uilizado fue: {primer_numero}')