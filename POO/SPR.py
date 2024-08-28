class Carro():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self,distancia):
        if self.tanque.obtener_gas() >= distancia /2:
            self.posicion += distancia
            self.tanque.usar_gas(distancia /2)
            print('has movido el carro exitosamente')
        else:
            print('no hay suficiente gas...')
    
    def obtener_posicion(self):
        return self.posicion
    
class TanqueDeGas:
    def __init__(self):
        self.gas = 100
    
    def meter_gas(self,cantidad):
        self.gas += cantidad
    
    def obtener_gas(self):
        return self.gas

    def usar_gas(self,cantidad):
        self.gas -= cantidad

tanque = TanqueDeGas()
carro = Carro(tanque)

print(carro.obtener_posicion())
print(carro.mover(10))
print(carro.obtener_posicion())
print(carro.mover(20))
print(carro.obtener_posicion())
print(carro.mover(80))
print(carro.obtener_posicion())
print(carro.mover(100))
print(carro.obtener_posicion())