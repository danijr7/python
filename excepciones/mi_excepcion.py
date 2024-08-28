class MiExcepcion(Exception):
          def __init__(self, error):
                  print(f'Entraste en mi propio error y fue: {error}')

try:
          raise MiExcepcion('acabo de probocar mi propio error con "raise"')
except:
          print('como pudiste comoter ese error?')