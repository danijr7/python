import matplotlib.pyplot as plt
numero = int(input('Ingrese un numero positivo, entero y mayor a 2: '))
num_ronda = 1
ronda = [num_ronda]
numero_usuario = [numero]
resultados = [numero_usuario,ronda]

while numero > 1:
          if (numero%2) == 0:#significa que es par
                    numero = numero / 2
          else:#sino es impar
                    numero = numero * 2 + 1
          num_ronda += 1
          ronda.append(num_ronda)
          numero_usuario.append(numero)
print(resultados)
""" plt.plot(ronda, numero_usuario, marker='*', linestyle='-')
plt.show() """