class Carro():
    def __init__(self):
        self._estado = 'apagado'
    
    def encender(self):
        self._estado = 'encendido'
        print(f'El carro esta: {self._estado}')
    
    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        print('Conduciendo...')

tesla = Carro()
tesla.conducir()