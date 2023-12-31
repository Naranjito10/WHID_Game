from random import randint
import random
from WHID_Ataques import *
import math
import sys

# PERSONAJE
class Personaje: 

    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, paciencia: int, estado = sin_estado):
        self.nombre = nombre
        self.energia = energia
        self.empatia = empatia
        self.dialectica = dialectica
        self.paciencia = paciencia
        self.estado = estado

    def esta_vivo(self):
        return self.energia > 0
    
    def morir(self):
        self.energia = 0
        self.estado = 0
        print(self.nombre, 'se ha quedado sin energía para seguir discutiendo.')
        if self.__class__.__name__ == 'Protagonista':
            print('No eres capaz de esforzarte por mantener a tu novia. Game Over')
            sys.exit()

    def ajustar_enfado_novia(self, ataque, novia):
        if novia.enfado + ataque.enfado > 100:
            novia.enfado = 100
        else:
            novia.enfado += ataque.enfado
    
    def ajustar_empatia(self, ataque):
        if self.__class__.__name__ == 'Boss':
            self.enfado += ataque.empatia
            print(f'El enfado de {self.nombre} ha subido a {self.enfado}')
        elif self.__class__.__name__ == 'Enemigo':
            self.empatia += ataque.empatia
            if ataque.empatia > 0:
                print(f'La empatía de {self.nombre} ha subido a {self.empatia}')
            elif ataque.empatia < 0:
                print(f'La empatía de {self.nombre} ha bajado a {self.empatia}')
            else:
                print(f'La empatía de {self.nombre} no ha cambiado')

    def comprobar_empatia(self, novia):
        if self.empatia > 50:
            print(f'{self.nombre} le ha hablado a {novia.nombre} bien sobre ti y ha bajado su enfado a {novia.enfado}')
            novia.enfado -= 10
        elif self.empatia < -50:
            print(f'{self.nombre} le ha hablado a {novia.nombre} sobre lo que le has dicho y ha subido su enfado a {novia.enfado}')
            novia.enfado += 10

    def aplicar_estado(self, ataque):
        if ataque.estado != sin_estado:
            self.comprobar_afectar_estado(ataque)

    def comprobar_afectar_estado(self, ataque):
        estado_afecta = ataque.estado.probabilidad_afectar_estado()

        if self.estado == sin_estado and estado_afecta:
            self.estado = ataque.estado
            print(f'{self.nombre} no tenía estado y ahora tiene el estado {ataque.estado.nombre} con un contador de {self.estado.contador}')

        elif self.estado != sin_estado and estado_afecta:
            if ataque.estado.nombre == self.estado.nombre: 
                self.estado.subir_contador()
                print(f'{self.nombre} ha incrementado su estado {ataque.estado.nombre} a {self.estado.contador}') 
            else: 
                print(f'{self.nombre} reemplaza su estado {self.estado.nombre}')
                self.estado = ataque.estado
                print(f'Ahora tiene el estado {ataque.estado.nombre}')

        elif self.estado == sin_estado and not estado_afecta:
            print(f'\n{self.nombre} no tiene ningún estado y no ha recibido el estado {ataque.estado.nombre}')

        elif self.estado != sin_estado and not estado_afecta:
            print(f'{self.nombre} tiene estado el estado {self.estado.nombre} y no ha sido afectado por el nuevo estado {ataque.estado.nombre}')
        
    def bajar_contador_estado(self):
        self.estado.contador -= 1
        print(f'El contador del estado ha bajado a {self.estado.contador}')
        if self.estado.contador == 0:
            print(f'{self.nombre} ya no tiene el estado {self.estado.nombre}\n')
            self.estado = sin_estado  
            self.estado.contador = 1  

    def daño_stun_estado(self):
        print(f'\n----- DAÑO ESTADO AL ATACANTE: {self.nombre} -----\n')
        efecto_stun = False
        if self.estado.nombre != 'Sin estado':
            print(f'{self.nombre} está {self.estado.nombre}')
            if self.estado.probabilidad_trigger_estado() == False:
                print(f'{self.estado.nombre} no hizo efecto')
                return efecto_stun
            
            if self.estado.daño == 0:
                print(f'{self.nombre} no recibe daño de {self.estado.nombre} porque su efecto es {self.estado.efecto}')
            else: 
                if self.estado.efecto == 'Veneno':
                    daño_efecto = self.estado.daño * self.estado.contador
                    self.energia -= daño_efecto
                else: 
                    daño_efecto = self.estado.daño
                    self.energia -= daño_efecto
                print(f'{self.nombre} ha recibido {daño_efecto} de daño por el estado {self.estado.nombre}. Ahora su energia es {self.energia}')
                self.bajar_contador_estado()
            
            if self.estado.efecto == 'Stun': 
                print(f'{self.nombre} está aturdido y no podrá atacar')    
                efecto_stun = True
                self.bajar_contador_estado()
                return efecto_stun
        else: 
            print(f'{self.nombre} no tiene estado')
        return efecto_stun
            
    def defender(self, contrincante, novia): 
        if contrincante.daño_stun_estado() == False:
            ataque_contrincante = contrincante.eleccion_ataque()
            daño_ataque_contrincante = self.calcular_daño(contrincante, ataque_contrincante)
            self.energia = self.energia - daño_ataque_contrincante
            print(f'\n----- ATAQUE DE {contrincante.nombre} -----\n')
            print(f'{contrincante.nombre} utiliza {ataque_contrincante.nombre}.')
            print(f'Argumenta con una fuerza total de {daño_ataque_contrincante}') 
            print(f'A {self.nombre} le baja la energía a {self.energia}\n')
            if self.__class__.__name__ != 'Protagonista':
                self.ajustar_empatia(ataque_contrincante)

            if self.esta_vivo == False: 
                self.morir()

            contrincante.ajustar_enfado_novia(ataque_contrincante, novia)
            self.aplicar_estado(ataque_contrincante)
        novia.novia_enfadada()

    def calcular_daño(self, contrincante, ataque_contrincante):
        daño = ataque_contrincante.daño * contrincante.dialectica 
        paciencia_anulada = 0
        # print(f'\n----- ESTADO DEL DEFENSOR: -----\n')
        print(f'\nEl estado de {self.nombre} es {self.estado.nombre}')
        if self.estado.nombre != 'Sin estado':
            print(f'{self.nombre} está {self.estado.nombre}')
            if self.estado.probabilidad_trigger_estado == False:
                # print(f'{self.estado.nombre} no hizo efecto para este ataque')
                pass
            
            else:
                if self.estado.efecto == 'Bajar armadura':
                    paciencia_anulada = self.paciencia
                    print(f'{self.nombre} ha perdido toda su paciencia para defenderse por el efecto {self.estado.efecto}')
                    self.bajar_contador_estado()
                else: 
                    # print(f'El estado {self.estado.nombre} tiene el efecto {self.estado.efecto} pero ahora no hace nada a {self.nombre}')
                    pass

        if contrincante.estado.efecto == 'Reducir daño':
            print(f'\nEl estado de {contrincante.nombre} es {contrincante.estado.nombre} con el efecto {contrincante.estado.efecto}')
            print(f'De este modo el daño de {contrincante.nombre} se reduce a la mitad')
            daño = math.floor(daño * 0.5)
            contrincante.bajar_contador_estado()

        if daño >= self.paciencia:
            daño = daño - self.paciencia + paciencia_anulada

        return daño

# CLASE HIJO PROTAGONISTA  
class Protagonista(Personaje):

    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, paciencia: int, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
        self.nivel = nivel
        self.experiencia = 0
        [seleccionar_nuevo_ataque(0) for _ in range(4)]
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Nivel: {self.nivel}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}, Paciencia: {self.paciencia}'
    
    def ganar_experiencia(self, cantidad, dificultad):
        self.experiencia += cantidad
        if self.nivel != 0:
            print(f'¡Has conseguido {cantidad} PA!')
        if self.nivel == 0:
            print('Llamaremos a los puntos de experiencia "Puntos de Amor" o "PA"')
        print(f'Ahora tienes {self.experiencia} PA.')
        print(f'Te faltan {self.calcular_experiencia_siguiente_nivel(dificultad) - self.experiencia} PA para subir al siguiente nivel.')
        while self.experiencia >= self.calcular_experiencia_siguiente_nivel(dificultad):
            self.subir_nivel()
        
    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        if self.nivel == 1:
            print(f'\nAhora eres nivel {self.nivel}, tus características son: ')
            print(self)
            print(f'\nEscoge entre estas dos habilidades para añadir a tu kit inicial: ')
            
        else: 
            print(f'\nAcabas de subir al nivel {self.nivel}')
            self.seleccionar_subida_caracteristicas()
            print(f'\nAhora tus características son: ')
            print(self)
            print(f'\nEscoge entre estas dos habilidades para añadir a tu kit: ')

        seleccionar_nuevo_ataque(self.nivel)

    def calcular_experiencia_siguiente_nivel(self, dificultad):
        return 25 * self.nivel * dificultad

    def seleccionar_subida_caracteristicas(self):
        característica_escogida = '0'
        while característica_escogida not in ['1', '2', '3', '4']:
            try:
                característica_escogida = input('''\nEscoge qué característica deseas incrementar:\n 
    - 1. Energía +10
    - 2. Empatía +5 
    - 3. Dialéctica +3
    - 4. Paciencia +2
                \nTu respuesta: ''')
            except ValueError:
                print('Debes escoger un número entre 1 y 4')

        if característica_escogida == '1':
            self.energia += 10
            print(f'Has subido tu energía a {self.energia}\n')
        elif característica_escogida == '2':
            self.empatia += 5
            print(f'Has subido tu empatía a {self.empatia}\n')
        elif característica_escogida == '3':
            self.dialectica += 3  
            print(f'Has subido tu dialéctica a {self.dialectica}\n')
        elif característica_escogida == '4':
            self.paciencia += 2
            print(f'Has subido tu paciencia a {self.paciencia}\n')
      
    def eleccion_ataque(self):
        print(f'\n----- ATAQUE DE {self.nombre} -----\n')
        print(f'Acciones disponibles:')
        print(f'\t- 1. Argumento razonable:')
        for i in AtaqueProta.arg_razonable:
            print(f'\t\t{i.nombre}')
            print(f'\t\t(Daño total: {i.daño * self.dialectica}, empatía: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})\n')
        
        print(f'\t- 2. Acción amistosa:')
        for i in AtaqueProta.acc_amistosa:
            print(f'\t\t{i.nombre}')
            print(f'\t\t(Daño total: {i.daño * self.dialectica}, empatía: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})\n')
            
        print(f'\t- 3. Ataque tóxico:')
        for i in AtaqueProta.arg_toxico:
            print(f'\t\t{i.nombre}')
            print(f'\t\t(Daño total: {i.daño * self.dialectica}, empatía: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})\n')
            
        print(f'\t- 4. Argumento cutre:')
        for i in AtaqueProta.arg_cutre:
            print(f'\t\t{i.nombre}')
            print(f'\t\t(Daño total: {i.daño * self.dialectica}, empatía: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})\n')
           
        ataque_elegido = '0'
        while ataque_elegido not in ['1', '2', '3', '4']:
            try: 
                ataque_elegido = input('Qué deseas realizar?: ')
            except ValueError:
                print('\nDebes escoger un número entre 1 y 4')

        if ataque_elegido == '1':
            categoria_elegida = AtaqueProta.arg_razonable
        elif ataque_elegido == '2':
            categoria_elegida = AtaqueProta.acc_amistosa
        elif ataque_elegido == '3':
            categoria_elegida = AtaqueProta.arg_toxico     
        elif ataque_elegido == '4':
            categoria_elegida = AtaqueProta.arg_cutre
        ataque_random = random.choice(categoria_elegida)
        print(f'{self.nombre} ataca con {ataque_random.nombre} con una fuerza de {ataque_random.daño * self.dialectica} y posibilidad de afectar con el estado {ataque_random.estado.nombre}')
        return ataque_random
         
# CLASE HIJO BOSS
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

    def __init__(self, nombre: str, energia: int, dialectica: int, enfado: int, paciencia: int, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia,dialectica, paciencia, estado)
        self.enfado = enfado
        self.nivel = nivel
        [seleccionar_nuevo_ataque_boss(self.nivel) for _ in range(4)]

    def __str__(self):
        return f'Nombre: {self.nombre}, Energía: {self.energia}, Dialéctica: {self.dialectica}, Enfado: {self.enfado}, Paciencia: {self.paciencia}'

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
        print(f'{self.nombre} ataca con {ataque_random.nombre} con una fuerza de {ataque_random.daño * self.dialectica} y posibilidad de afectar con el estado {ataque_random.estado.nombre}')
        return ataque_random
    
    def novia_enfadada(self):
        if self.enfado >= 100: 
            print('El nivel de enfado de la novia es demasiado alto. Tu novia te ha dejado. Game Over.')
            sys.exit()         
        
# CLASE HIJO ENEMIGO 
class Enemigo(Personaje):
    
    lista_ataques_enemigo = []
    
    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, paciencia: int, ataque_enemigo: str, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
        self.ataque_enemigo = ataque_enemigo
        self.nivel = nivel

    def __str__(self):
        return f'Nombre: {self.nombre}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}, Ataque: {self.ataque_enemigo}, Paciencia: {self.paciencia}'
    
    def eleccion_ataque(self):
        print(f'{self.nombre} ataca con {self.ataque_enemigo.nombre} con una fuerza de {self.ataque_enemigo.daño * self.dialectica} y posibilidad de afectar con el estado {self.ataque_enemigo.estado.nombre}')
        return self.ataque_enemigo

# ALIADO
class Aliado():

    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __str__(self):
        return f'Nombre: {self.nombre}'

    def eleccion_personaje(self, personaje, novia):
        # El PADRE te da un consejo y te da una nueva habilidad
        if self.nombre == 'Padre':
            print(f'Tu padre te ofrece dos herramientas para mitigar el enfado de tu novia. ¿Cuál escoges?')
            seleccionar_nuevo_ataque(personaje.nivel)
            print('Tu padre te ha dado un par de consejos y te sientes más seguro de ti mismo')

        # La MADRE te da un consejo y te sube una
        elif self.nombre == 'Madre':
            print('Tu madre te explica que no es bueno discutir con tu novia, es mejor hablar las cosas tranquilamente')
            personaje.seleccionar_subida_caracteristicas()
            print('Tu madre siempre es sabia y te sientes más seguro de ti mismo')

        # La ABUELA te da de comer y te sube la energía y alguna característica
        elif self.nombre == 'Abuela':
            comida = '0'
            while comida not in ['1', '2', '3', '4']:
                try:
                    comida = input('''Tu abuela te pregunta que quieres para comer: \n         
    - 1. Lentejas (+20 energía)
    - 2. Tortilla (+10 empatía, +10 energía)
    - 3. Macarrones (+10 dialéctica, +10 energía)
    - 4. Pescado (+5 empatía, +5 dialéctica)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 4')

            if comida == '1':
                print('Tu abuela te ha hecho unas lentejas y te sientes más fuerte')
                personaje.energia += 20
            elif comida == '2':
                print('Tu abuela te ha hecho una tortilla y te sientes más fuerte')
                personaje.empatia += 10
                personaje.energia += 10
            elif comida == '3':
                print('Tu abuela te ha hecho unos macarrones y te sientes más fuerte')
                personaje.dialectica += 10
                personaje.energia += 10
            elif comida == '4':
                personaje.dialectica += 5
                personaje.empatia += 5
                print('Tu abuela te ha hecho pescado y te sientes más fuerte')
        
        # El ABUELO te cuenta una historia y te sube de nivel pero te baja la empatía y sube el enfado de tu novia
        elif self.nombre == 'Abuelo':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu abuelo te cuenta la historia de cuando era joven y tu abuela se enfadó muchísimo con él. 
    Qué lástima que sean tiempos tan distintos... ¿Quieres seguir sus consejos?:\n                        
    - 1. Sí (-15 empatía, +1 nivel)
    - 2. No (+20 energía)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Tu abuelo te ha contado una historia y te sientes más fuerte pero con ideas anticuadas.')
                personaje.empatia -= 10
                print(f'Ahora tu empatía es {personaje.empatia}.')
                personaje.subir_nivel()
            elif eleccion == '2':
                print('Piensas que tu abuelo tiene ideas anticuadas y no le haces caso. Al menos te ha dado chuches.')
                personaje.energia += 20
                personaje.empatia += 5
                print(f'Ahora tu energía es {personaje.energia} y tu empatía es {personaje.empatia}.')

        # El AMIGO te da un consejo y te sube la dialectica
        elif self.nombre == 'Amigo':
            print('Tu amigo intenta darte un consejo pero no se le ocurre nada. Al menos te ha dado un Sed Buy.')
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Si decides bebértelo, tu dialéctica subirá, pero tu empatía bajará. ¿Quieres bebértelo?\n
    - 1. Sí (+10 dialéctica, -10 empatía)
    - 2. No (No pasa nada)
    \n¿Qué haces?: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Te sientes más despierto y con más energía, tienes ganas de discutir.')
                personaje.dialectica += 10
                print(f'Ahora tu dialéctica es {personaje.dialectica}.')

        # Tu AMIGA te invita a su casa a ver una peli y te sube la energía y la empatía pero sube el enfado de tu novia
        elif self.nombre == 'Amiga':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Tu amiga quiere que te vayas a su casa a ver una peli para calmarte. ¿Aceptas?
    - 1. Sí
    - 2. No
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')

            if eleccion == '1':
                print('Veis Shreck y te sientes mucho más comprendido y con energía. Que pena que te vieron con tu amiga...')
                personaje.energia += 40
                personaje.paciencia += 2
                personaje.empatia += 1
                novia.enfado += 10
                print(f'Ahora tu energía es {personaje.energia}, tu paciencia es {personaje.paciencia} y tu empatía es {personaje.empatia}. Pero el enfado de tu novia ha subido a {novia.enfado}.')

            elif eleccion == '2':
                print('Tu amiga te dice que no te preocupes, que te va a ayudar a salir de esta.')
                personaje.dialectica += 5
                print(f'Ahora tu dialéctica es {personaje.dialectica}.')
        
        # Tu HERMANO te invita a jugar al futbol o a tomar unas cervezas
        elif self.nombre == 'Hermano':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Tu hermano te dice de hacer algo con él para que te distraigas. ¿Qué prefieres?\n                  
    - 1. Ir a jugar al futbol (-10 energía, +10 empatía)
    - 2. Ir a tomar unas cervezas (+20 energía, -5 dialéctica)
    \nTu respuesta: ''') 
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
  
            if eleccion == '1':
                print('El partido te ha cansado un poco pero te sientes más empático.')
                personaje.energia -= 10
                personaje.empatia += 10
                print(f'Ahora tu empatía es {personaje.empatia} y tu energía es {personaje.energia}.')
            elif eleccion == '2':
                print('Te sientes achispado pero te cuesta algo vocalizar tus argumentos.')
                personaje.energia += 30
                personaje.dialectica -= 5
                print(f'Ahora tu dialéctica es {personaje.dialectica} y tu energía es {personaje.energia}.')
            
        # Tu HERMANA te invita a ir de compras o a un escape room
        elif self.nombre == 'Hermana':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Tu hermana entiende perfectamente la situación y te da un abrazo. 
    Te ofrece un par de planes para desconectar:
                             
    - 1. Ir de compras (-10 energía, +5 empatía, +5 dialéctica)
    - 2. Ir a un Escape Room (-20 energía, +3 paciencia)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Te sientes más carismático.')
                personaje.energia -= 10
                personaje.empatia += 5
                personaje.dialectica += 5
                print(f'Ahora tu empatía es {personaje.empatia}, tu dialéctica es {personaje.dialectica} y tu energía es {personaje.energia}.')
            elif eleccion == '2':
                print('Te sientes más tranquilo.')
                personaje.energia -= 20
                personaje.paciencia += 3
                print(f'Ahora tu paciencia es {personaje.paciencia} y tu energía es {personaje.energia}.')
        
        # Tu PERRO te da un lametón y te sube la paciencia o la empatía
        elif self.nombre == 'Perro':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu perro te da un lametón en la cara ya que te ve triste. ¿Qué haces?\n
    - 1. Lo sacas a pasear. (+2 paciencia)
    - 2. Lo acaricias y juegas con él. (+5 empatía)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Dar una vuelta con tu perro te ha relajado.')
                personaje.paciencia += 2
                print(f'Ahora tu energía es {personaje.energia}.')
            elif eleccion == '2':
                print('Pasar un rato con tu perro te ha hecho sentir más alegre.')
                personaje.empatia += 5
                print(f'Ahora tu energía es {personaje.energia}.')

        elif self.nombre == 'Gato':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu gato está acurrucado en tu cama. ¿Qué haces?\n
    - 1. Lo agarras y lo mimas hasta que te araña por pesado. (-10 energia, +10 empatía)
    - 2. Sacas un cordel y juegas con él. (+15 energia, +1 empatía)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Tu gato te ha arañado y pero ha merecido la pena')
                personaje.energia -= 10
                personaje.empatia += 10
                print(f'Ahora tu energía es {personaje.energia} y tu empatía es {personaje.empatia}.')
            elif eleccion == '2':
                print('Tu gato se ha cansado y se ha dormido pero tú has recuperado fuerzas.')
                personaje.energia += 15
                personaje.empatia += 1
                print(f'Ahora tu energía es {personaje.energia} y tu empatía es {personaje.empatia}.')
                
        elif self.nombre == 'Compañero de clase':
            print('Tu compañero te pregunta qué tal estás y si tienes papel. ¿Qué le dices?')
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu compañero bromea diciéndote que tu novia está preciosa, que si se la prestas para "calmarla". ¿Qué haces?\n
    - 1. Te peleas con él. (Borras una habilidad de tu kit)
    - 2. Sudas de su cara. (Augmentas tu paciencia en 2)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('De un puñetazo que recibes te olvidas de como argumentar correctamente.')
                seleccionar_habilidad_borrar()
            elif eleccion == '2':
                print('Tu autocontrol es envidiable.')
                personaje.paciencia += 2
                print(f'Ahora tu paciencia es {personaje.paciencia}.')
        
        elif self.nombre == 'Compañera de clase':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu compañera te dice de acompañarla al baño de chicas para contarte un secretito. ¿Qué le dices?\n
    - 1. Aceptas. (Sorpresa)
    - 2. Le dices que no porque desconfias de sus intenciones. (Sorpresa)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Tu novia te ha visto y ha pensado que te estabas enrollando con ella. Su enfado ha subido. Además, tu compañera te ha contado un secreto que no te importaba.')
                novia.enfado += 10
                personaje.energia -= 20
                personaje.paciencia += 2
                print(f'Ahora tu energia es {personaje.energia} y tu paciencia es {personaje.paciencia}. El enfado de tu novia es {novia.enfado}.')
            elif eleccion == '2':
                print('Tu novia te ha visto y ha pensado que eres un buen chico. Su enfado ha bajado.')
                novia.enfado -= 10
                print(f'Ahora el enfado de tu novia es {novia.enfado}.')
        

                
    
    