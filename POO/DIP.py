""" class Diccionario:
    def verf_palb(self,palabra):
        #logica para verificar palabra
        pass

class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()
    
    def corregir_text(self,texto):
        #usamos el usuario para corregir el texto
        pass """

from abc import ABC, abstractmethod

class VerfOrtgr(ABC):
    @abstractmethod
    def verf_palb(self,palabra):
        pass

class Diccionario(VerfOrtgr):
    def verf_palb(self, palabra):
        #logica verificadora
        pass

class CorrectoOrtg:
    def __init__(self, verificador):
        self.verificador = verificador
    
    def corregir_txt(self, texto):
        #log verf
        pass

corrector = CorrectoOrtg(Diccionario())