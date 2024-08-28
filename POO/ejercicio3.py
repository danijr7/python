class Jugador:
    def __init__(self,nombre,apellido,pase,tiro,defensa,ritmo,regate,fisico):
        self.nombre = nombre
        self.apellido = apellido
        self.pase = pase
        self.tiro = tiro
        self.defensa = defensa
        self.ritmo = ritmo
        self.regate = regate
        self.fisico = fisico
    
    def __repr__(self):
        return f"""
                -Nombre: {self.nombre}\n
                -Apellido: {self.apellido}\n
                -Pase: {self.pase}\n
                -Tiro: {self.tiro}\n
                -Defensa: {self.defensa}\n
                -Ritmo: {self.ritmo}\n
                -Regate: {self.regate}\n
                -Fisico: {self.fisico}\n
                """
    
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + '-' + otro_pj.nombre
        nuevo_apellido = self.apellido + '-' + otro_pj.apellido
        nuevo_pase = (self.pase + otro_pj.pase)/2
        nuevo_tiro = (self.tiro + otro_pj.tiro)/2
        nueva_defensa = (self.defensa + otro_pj.defensa)/2
        nuevo_ritmo = (self.ritmo + otro_pj.ritmo)/2
        nuevo_regate = (self.regate + otro_pj.regate)/2
        nuevo_fisico = (self.fisico + otro_pj.fisico)/2
        return Jugador(nuevo_nombre,nuevo_apellido,nuevo_pase,nuevo_tiro,nueva_defensa,nuevo_ritmo,nuevo_regate,nuevo_fisico)

lionesMessi = Jugador('Lionel','Messi',88,97,48,90,96,77)
cristianoRonaldo = Jugador('Cristiano','Ronaldo',90,99,65,99,99,99)
neymar = Jugador('Neymar',"Jr.",89,97,60,94,100,86)

superJugador = lionesMessi + cristianoRonaldo + neymar
print(superJugador)