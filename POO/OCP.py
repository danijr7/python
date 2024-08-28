class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mansaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorMail(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por MAIL a {self.usuario.mail}')

class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por SMS a {self.usuario.sms}')

#etc...