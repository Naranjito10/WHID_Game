class Personaje: 

    def __init__(self, nombre, energia, empatia, dialectica):
        self.nombre = nombre
        self.energia = energia
        self.empatia = empatia
        self.dialectica = dialectica
            
    def __str__(self):
        return f"Nombre: {self.nombre}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}"
    
    def atacar(self, ataque_propio):
        print(f"{self.nombre} ataca con una fuerza de {ataque_propio}")
        resultado = self.dialectica * ataque_propio
        return resultado
    
    def defender(self, ataque_contrincante): 
        # self.paciencia - ataque_contrincante
        resultado = self.energia - ataque_contrincante
        self.energia = resultado
        print(f"{self.nombre} defiende contra un ataque de {ataque_contrincante} y le baja la energia a {resultado}")
        return resultado
        

class Enemigo(Personaje):
    pass
