def suma():
          while True:
                    a = input('Numero 1: ')
                    b = input('Numero 2: ')
                    try:
                              resultado = int(a) + int(b)
                    except ValueError as e:
                              print('-entraste en la excepcion pq hya un ValueError')
                              print(f'-la excepcion que occurio fue: {e}')
                    except ZeroDivisionError:
                              print('-entraste en la excepcion porque dividiste /0')
                    else:
                              break
                    finally:
                              print('*esto es el "finally" que se ejecuta siempre')
          return resultado
print(suma())