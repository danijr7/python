ingreso = 100
gasto = 51000
saldo = ingreso - gasto

#if anidados y else if (elif)
if ingreso > 10000:
          print('estas bien en cualquier parte del mundo')
          if ingreso - gasto > 3000:
                    print('y esta bien gastar eso')
          elif saldo < 0:
                    print(f'pero tienes un deifit de {saldo} :(')
          else:
                    print('pero no deberias gastar tanto')
elif ingreso > 1000:
          print('estas bien en paises tercer mundistas') #puedo poner cuantos 'elif' quiera
else:
          print('ponete a trabajar maldita sanquijuela del estado')