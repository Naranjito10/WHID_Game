from random import randint
import random
from WHID_Ataques import *

class Personaje: 

    def __init__(self, nombre, energia, empatia, dialectica):
        self.nombre = nombre
        self.energia = energia
        self.empatia = empatia
        self.dialectica = dialectica
        self.estado = 0
            
    def __str__(self):
        return f"Nombre: {self.nombre}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}"
        
    # def subir_nivel(self, energia, empatia, dialectica):
    #     self.energia = self.energia + energia
    #     self.empatia = self.empatia + empatia
    #     self.dialectica = self.dialectica + dialectica
    #     print(f"Has subido de nivel. Tus características son: Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}")

    def esta_vivo(self):
        return self.energia > 0
    
    def morir(self):
        self.energia = 0
        print(self.nombre, "se ha quedado sin energia para seguir discutiendo")

    def ataque(self): 
        daño, estado = self.eleccion_ataque()
        print('\n')
        resultado = self.dialectica * daño
        print(f"{self.nombre} ataca con una fuerza total de {resultado}")
        return resultado
    
    def defender(self, ataque_contrincante, estado): 
        self.energia = self.energia - ataque_contrincante
        print(f"{self.nombre} recibe el argumento {ataque_contrincante} y le baja la energia a {self.energia}")
        if self.energia < 0:
            print('Has acabado con la energia del enemigo')
        elif estado != 0:
            self.aplicar_estado(estado)
    
    # def trigger_estado(self, estado):
    #     if estado.probabilidad_trigger > random.random():
    #         print(f"{self.nombre} ha recibido daño de {estado.nombre}")
    #         self.estado = estado
    
    def aplicar_estado(self, estado):
        
        print(f"{self.nombre} ha recibido el estado {estado.nombre}")
        self.estado = estado

        
class Protagonista(Personaje):

    lista_ataques_prota = []

    def __init__(self, nombre, energia, empatia, dialectica, nivel):
        super().__init__(nombre, energia, empatia, dialectica)
        self.nivel = nivel
        seleccionar_nuevo_ataque(0)
        seleccionar_nuevo_ataque(0)
        seleccionar_nuevo_ataque(0)
        seleccionar_nuevo_ataque(0)
        

    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'\nAhora eres nivel {self.nivel}, tus características son: ')
            print(self)
            print(f'\nEscoge entre estas dos habilidades para añadir a tu kit inicial: ')
            
        else: 
            print(f'\nAcabas de subir al nivel {self.nivel}, tus características son: ')
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
        probabilidad = ataque_random.estado.probabilidad_afectar
        if probabilidad > 0.1:
            print(f"{self.nombre} ataca con '{ataque_random.nombre}' con una fuerza de {ataque_random.daño} y aplica el estado {ataque_random.estado.nombre}")
            return ataque_random.daño, ataque_random.estado
        else:
            print(f"{self.nombre} ataca con '{ataque_random.nombre}' con una fuerza de {ataque_random.daño}")
            return ataque_random.daño, 0
         


class Boss(Personaje):

    lista_ataques_boss = []

    lista_veredictos = [
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

    def __init__(self, nombre, energia, empatia, dialectica, enfado, nivel):
        super().__init__(nombre, energia, empatia, dialectica)
        self.enfado = enfado
        self.nivel = nivel
        seleccionar_nuevo_ataque_boss(0)
        seleccionar_nuevo_ataque_boss(0)
        seleccionar_nuevo_ataque_boss(0)
        seleccionar_nuevo_ataque_boss(0)

    def __str__(self):
        return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatia}, Dialectica: {self.dialectica}, Enfado: {self.enfado}"

    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'\nAhora eres nivel {self.nivel}, escoge entre estas dos habilidades para añadir a tu kit inicial: ')
        else: 
            print(f'\nAcabas de subir al nivel {self.nivel}, escoge entre estas dos habilidades para añadir a tu kit: ')

        seleccionar_nuevo_ataque(self.nivel)
    
    def eleccion_ataque(self):
        ataque_random = random.choice(AtaqueBoss.lista_ataques_boss)
        print('Ataque boss')
        probabilidad = ataque_random.estado.probabilidad_afectar
        print(ataque_random.estado.nombre)
        print(probabilidad)
        if probabilidad > random.random():
            print(f"{self.nombre} ataca con '{ataque_random.nombre}' con una fuerza de {ataque_random.daño * self.dialectica} y aplica el estado {ataque_random.estado.nombre}")
            return ataque_random.daño, ataque_random.estado
        else:
            print(f"{self.nombre} ataca con '{ataque_random.nombre}' con una fuerza de {ataque_random.daño * self.dialectica}")
            return ataque_random.daño, 0
   
        
        
class Enemigo(Personaje):
    
        lista_ataques_enemigo = []
        
        def __init__(self, nombre, energia, empatia, dialectica, enfado, ataque_enemigo):
            super().__init__(nombre, energia, empatia, dialectica)
            self.enfado = enfado
            self.ataque_enemigo = ataque_enemigo
    
        def __str__(self):
            return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatia}, Dialectica: {self.dialectica}, Enfado: {self.enfado}"
    
        # def eleccion_ataque(self):
        # daño =  self.ataque_enemigo.daño
        # suegro.ataque_enemigo.dañoself.lista_ataques_boss)
        # print('Ataque boss')
        # probabilidad = ataque_random.estado.probabilidad_afectar
        # print(ataque_random.estado.nombre)
        # print(probabilidad)
        # if probabilidad > random.random():
        #     print(f"{self.nombre} ataca con '{ataque_random.nombre}' con una fuerza de {ataque_random.daño * self.dialectica} y aplica el estado {ataque_random.estado.nombre}")
        #     return daño, ataque_random.estado
        # else:
        #     print(f"{self.nombre} ataca con '{ataque_random.nombre}' con una fuerza de {ataque_random.daño * self.dialectica}")
        #     return daño, 0