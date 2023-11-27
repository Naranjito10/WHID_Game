class Personaje: 

    def __init__(self, nombre, paciencia, empatía, labia, enfado):
        self.nombre = nombre
        self.paciencia = paciencia
        self.empatía = empatía
        self.labia = labia
        self.enfado = enfado
            
    def __str__(self):
        return f"Nombre: {self.nombre}, Paciencia: {self.paciencia}, Empatía: {self.empatía}, Labia: {self.labia}, Enfado: {self.enfado}"
    
    def atacar(self, ataque_propio):
        print(f"{self.nombre} ataca con una fuerza de {ataque_propio}")
        resultado = self.labia * ataque_propio
        return resultado
    
    def defender(self, ataque_contrincante): 
        # self.paciencia - ataque_contrincante
        resultado = self.paciencia - ataque_contrincante
        self.paciencia = resultado
        print(f"{self.nombre} defiende contra un ataque de {ataque_contrincante} y le baja la paciencia a {resultado}")
        return resultado
        

class Enemigo(Personaje):
    pass
