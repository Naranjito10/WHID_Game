from random import randint
import random
from WHID_Ataques import *

class Personaje: 

    def __init__(self, nombre, energia, empatia, dialectica, paciencia):
        self.nombre = nombre
        self.energia = energia
        self.empatia = empatia
        self.dialectica = dialectica
        self.paciencia = paciencia
        self.estado = 0
            
    def __str__(self):
        return f"Nombre: {self.nombre}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}"

    def esta_vivo(self):
        return self.energia > 0
    
    def morir(self):
        self.energia = 0
        print(self.nombre, "se ha quedado sin energia para seguir discutiendo")

    def defender(self, ataque_contrincante, dialectica): 
        daño = ataque_contrincante.daño * dialectica
        self.energia = self.energia - daño
        print(f"{self.nombre} recibe el argumento {ataque_contrincante} con una fuerza total de {daño} y le baja la energia a {self.energia}")
        if self.energia <= 0:
            print('Has acabado con la energia del enemigo')
        elif self.energia > 0:
            self.comprobar_afectar_estado(ataque_contrincante)
    
    def comprobar_afectar_estado(self, ataque):
        if ataque.estado != 0:
            if self.estado == 0 and ataque.estado.probabilidad_afectar_estado():
                self.estado = ataque.estado
                print(f"{self.nombre} ha sido afectado por el estado {ataque.estado.nombre}")

            elif self.estado != 0 and self.estado != ataque.estado:
                if ataque.estado.probabilidad_afectar_estado():
                    self.estado = ataque.estado
                    print(f"{self.nombre} ha sido afectado por el estado {ataque.estado.nombre}")
                else:
                    print(f"{self.nombre} no ha sido afectado por el estado {ataque.estado.nombre}")

    def trigger_estado(self):
        if self.estado != 0:
            print(self.estado)
            print(self.estado.daño)
            if self.estado.probabilidad_trigger_estado:
                self.energia -= self.estado.daño
                print(f"{self.nombre} ha recibido {self.estado.daño} de daño por el estado {self.estado.nombre}")
            else:
                print(f"{self.nombre} no ha recibido daño por el estado {self.estado.nombre}")



# PERSONAJES  
class Protagonista(Personaje):

    def __init__(self, nombre, energia, empatia, dialectica, paciencia, nivel):
        super().__init__(nombre, energia, empatia, dialectica, paciencia)
        self.nivel = nivel
        [seleccionar_nuevo_ataque(0) for _ in range(4)]
        
    def seleccionar_subida_habilidad(self):
        print(f'\nAcabas de subir al nivel {self.nivel}')
        característica_escogida = input('''Escoge qué característica deseas incrementar: 
                - 1. Energia +10
                - 2. Empatía +5 
                - 3. Dialectica +5
                - 4. Paciencia +2
              ''')

        if característica_escogida == '1':
            self.energia += 10
            print(f'Has subido tu energía a {self.energia}')
        elif característica_escogida == '2':
            self.empatia += 5
            print(f'Has subido tu empatía a {self.empatia}')
        elif característica_escogida == '3':
            self.dialectica += 5    
            print(f'Has subido tu dialectica a {self.dialectica}')
        elif característica_escogida == '4':
            self.paciencia += 2
            print(f'Has subido tu paciencia a {self.paciencia}')

    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'\nAhora eres nivel {self.nivel}, tus características son: ')
            print(self)
            print(f'\nEscoge entre estas dos habilidades para añadir a tu kit inicial: ')
            
        else: 
            self.seleccionar_subida_habilidad()
            print(f'\nAhora tus características son: ')
            print(self)
            print(f'\nEscoge entre estas dos habilidades para añadir a tu kit: ')

        seleccionar_nuevo_ataque(self.nivel)
        
    def eleccion_ataque(self):
        print('''Acciones disponibles: 
                - 1. Argumento razonable
                - 2. Acción amistosa 
                - 3. Ataque toxico 
                - 4. Argumento cutre
              ''')
        ataque_elegido = input('Qué deseas realizar?: ')
        if ataque_elegido == '1':
            categoria_elegida = AtaqueProta.arg_razonable
        elif ataque_elegido == '2':
            categoria_elegida = AtaqueProta.acc_amistosa
        elif ataque_elegido == '3':
            categoria_elegida = AtaqueProta.arg_toxico     
        elif ataque_elegido == '4':
            categoria_elegida = AtaqueProta.arg_cutre
        ataque_random = random.choice(categoria_elegida)
        return ataque_random
         

# BOSS
class Boss(Personaje):

    lista_ataques_boss = []

    lista_motivos = [
        'Le diste like a una amiga en instagram.', 
        'Te vio hablando con una amiga en la calle.', 
        'No le escribiste mientras estabas de viaje.', 
        'Ha visto que sigues hablando con tu ex de forma cariñosa.', 
        'Te vio online en whatsapp y que no le contestaste.',
        'Te acabaste la nutella que quedaba.',
        'Te dejaste la luz del baño encendida.',
        'Te dejaste la tapa del váter subida.',
        '¿Has utilizado mi champú ultra caro?',
        '¿Te has visto más capítulos de nuestra serie sin mí?',
        '¿Por qué te has gastado 100€ euros en un videojuego?',
        'Ayer en vez de venir a dormir conmigo te quedaste hasta las tantas jugando al lol con tus amigos.'
    ]

    def __init__(self, nombre, energia, empatia, dialectica, enfado, paciencia, nivel):
        super().__init__(nombre, energia, empatia, dialectica, paciencia)
        self.enfado = enfado
        self.nivel = nivel
        [seleccionar_nuevo_ataque_boss(self.nivel) for _ in range(4)]

    def __str__(self):
        return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatia}, Dialectica: {self.dialectica}, Enfado: {self.enfado}, Paciencia: {self.paciencia}"

    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'\nAhora el Boss es nivel {self.nivel}')
        else: 
            print(f'\nAcabas el Boss es nivel {self.nivel}')

        seleccionar_nuevo_ataque_boss(self.nivel)
    
    def eleccion_ataque(self):
        ataque_random = random.choice(AtaqueBoss.lista_ataques_boss)
        print('Ataque boss')
        print(f"{self.nombre} ataca con '{ataque_random.nombre}' con una fuerza de {ataque_random.daño * self.dialectica}")
        return ataque_random
        
# CLASE ENEMIGO 
class Enemigo(Personaje):
    
    lista_ataques_enemigo = []
    
    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, enfado: int, ataque_enemigo: str, paciencia: int, nivel: int):
        super().__init__(nombre, energia, empatia, dialectica, paciencia)
        self.enfado = enfado
        self.ataque_enemigo = ataque_enemigo

    def __str__(self):
        return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatia}, Dialectica: {self.dialectica}, Enfado: {self.enfado}, Ataque: {self.ataque_enemigo}, Paciencia: {self.paciencia}"
    
    def eleccion_ataque(self):
        print('Ataque Enemigo: ')
        print(f"{self.nombre} ataca con '{self.ataque_enemigo.nombre}' con una fuerza de {self.ataque_enemigo.daño * self.dialectica}")
        return self.ataque_enemigo
        
# CLASE ALIADO
class Aliado():

    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __str__(self):
        return f"Nombre: {self.nombre}"

    def habilidad_padre(self, personaje, nivel):
        return personaje.seleccionar_nuevo_ataque(nivel)

    def habilidad_madre(self, personaje, nivel):
        return personaje.seleccionar_nuevo_ataque(nivel)

    # def eleccion_personaje(self, personaje, nivel):
    #     if self.nombre == 'Padre':
    #         hola = self.habilidad_padre(personaje, nivel)
    #     elif self.nombre == 'Madre':
    #         hola = self.habilidad_madre(personaje, nivel)
    #         pass
    
    
    