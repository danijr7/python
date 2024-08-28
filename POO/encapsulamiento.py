class MiClase:
    def __init__(self):
        #valor privado
        self.__atributo_privado = 'valor'
        
    #metodo privado
    def __hablar(self):
            print('q tal chavales')
        

objeto = MiClase()
print(objeto.__hablar)