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
            
    def __str__(self):
        return f"Nombre: {self.nombre}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}"

    def esta_vivo(self):
        return self.energia > 0
    
    def morir(self):
        self.energia = 0
        self.estado = 0
        print(self.nombre, "se ha quedado sin energía para seguir discutiendo. GANASTE LA DISCUSIÓN.")
        sys.exit()

    def ajustar_enfado_novia(self, ataque, novia):
        if novia.enfado + ataque.enfado > 100:
            novia.enfado = 100
        else:
            novia.enfado += ataque.enfado
    
    def ajustar_empatia(self, ataque):
        if self.__class__.__name__ == 'Boss':
            self.enfado += ataque.empatia
        elif self.__class__.__name__ == 'Enemigo':
            self.empatia += ataque.empatia

    def comprobar_empatia(self, novia):
        if self.empatia > 50:
            print(f"{self.nombre} ha conseguido que {novia.nombre} se sienta comprendida y ha bajado su enfado")
            novia.enfado -= 10
        elif self.empatia < -50:
            print(f"{self.nombre} ha conseguido que {novia.nombre} se sienta incomprendida y ha subido su enfado")
            novia.enfado += 10

    def comprobar_muerte_aplicar_estado(self, ataque):
        if self.esta_vivo:
            if ataque.estado != sin_estado:
                self.comprobar_afectar_estado(ataque)
        else:
            self.morir()

    def comprobar_afectar_estado(self, ataque):
        estado_afecta = ataque.estado.probabilidad_afectar_estado()

        if self.estado == sin_estado and estado_afecta:
            self.estado = ataque.estado
            print(f"{self.nombre} ha sido afectado por el estado {ataque.estado.nombre}")

        elif self.estado != sin_estado and estado_afecta:
            if ataque.estado.nombre == self.estado.nombre: 
                self.estado.subir_contador()
                print(f"{self.nombre} ha incrementado su estado {ataque.estado.nombre}") 
            else: 
                print(f"{self.nombre} reemplaza su estado {self.estado.nombre}")
                self.estado = ataque.estado
                print(f"{self.nombre} ha sido afectado por el estado {ataque.estado.nombre}")

        elif self.estado == sin_estado and not estado_afecta:
            print(f"{self.nombre} está limpio de estados y no ha recibido el estado {ataque.estado.nombre}")

        elif self.estado != sin_estado and not estado_afecta:
            print(f"{self.nombre} tiene estado y no ha sido afectado por el nuevo estado {ataque.estado.nombre}")
        
    def comprobar_contador_a_0(self):
        if self.estado.bajar_contador():
            print(f"{self.nombre} ya no tiene el estado {self.estado.nombre}\n")
            self.estado = sin_estado

    # ! no funciona
    def defender(self, contrincante, stun_contrincante, novia): 
        if stun_contrincante:
            daño_ataque_contrincante, stun_recibido_por_estado = self.calcular_daño(contrincante, stun_activado)
            if not self.esta_vivo: 
                self.morir()
            print(f"{contrincante.nombre} está paralizado y no puede atacar")
            novia.novia_enfadada()
            return stun_recibido_por_estado
        else: 
            ataque_contrincante = contrincante.eleccion_ataque()
            daño_ataque_contrincante, stun_recibido_por_estado = self.calcular_daño(contrincante, ataque_contrincante)
            self.energia = self.energia - daño_ataque_contrincante
            print('\n----- Apartado sobre el ataque del atacante -----\n')
            print(f"{self.nombre} recibe el argumento {ataque_contrincante.nombre} con una fuerza total de {daño_ataque_contrincante} y le baja la energía a {self.energia}")
            contrincante.ajustar_enfado_novia(ataque_contrincante, novia)
            if self.__class__.__name__ != 'Protagonista':
                self.ajustar_empatia(ataque_contrincante)
            self.comprobar_muerte_aplicar_estado(ataque_contrincante)
            contrincante.ajustar_enfado_novia(ataque_contrincante, novia)
            novia.novia_enfadada()
            return stun_recibido_por_estado

    def calcular_daño(self, contrincante, ataque_contrincante):
        daño = ataque_contrincante.daño * contrincante.dialectica 
        efecto_stun = False
        paciencia_anulada = 0
        print('\n----- Apartado sobre el estado del que defiende -----\n')
        print(f'El estado de {self.nombre} es {self.estado.nombre}')
        if self.estado != sin_estado:
            print(f'{self.nombre} está {self.estado.nombre}')
            if self.estado.probabilidad_trigger_estado == False:
                print(f"{self.estado.nombre} no surgió efecto")
            
            if self.estado.probabilidad_trigger_estado:
                if self.estado.efecto == 'Sin efecto':
                    print(f'El efecto del estado es nulo, este MENSAJE NO debería aparecer')

                elif self.estado.efecto == 'Sofocado':
                    efecto_stun = True
                    print(f'{self.nombre} está sofocado y no podrá atacar')
                    self.comprobar_contador_a_0()

                elif self.estado.efecto == 'Stun': 
                    self.comprobar_contador_a_0()
                    print(f'{self.nombre} está aturdido y no podrá atacar')
                    efecto_stun = True

                elif self.estado.efecto == 'Bajar armadura':
                    paciencia_anulada = self.paciencia
                    print(f'{self.nombre} ha perdido toda su paciencia')
                    self.comprobar_contador_a_0()

                if self.estado.daño != 0:
                    if self.estado.efecto == 'Veneno':
                        daño_efecto = self.estado.daño * self.estado.contador
                        self.energia -= daño_efecto
                    else: 
                        daño_efecto = self.estado.daño
                        self.energia -= daño_efecto

                    self.comprobar_contador_a_0()
                    print(f"{self.nombre} ha recibido {daño_efecto} de daño por el estado {self.estado.nombre}. Ahora su energia es {self.energia}")
                else: 
                    print(f"{self.nombre} ha sido afectado por el estado {self.estado.nombre}. Su efecto es {self.estado.efecto}")
            else: 
                print(f"{self.nombre} NONONO ha sido afectado por el estado {self.estado.nombre}. Su efecto es {self.estado.efecto}")
        else: 
            print(f'{self.nombre} no tiene estados')
        
        if contrincante.estado != sin_estado and contrincante.estado.efecto == 'Reducir daño':
            daño = math.floor(daño * 0.5)

        if daño >= self.paciencia:
            daño = daño - self.paciencia + paciencia_anulada

        return daño, efecto_stun

# CLASE HIJO PROTAGONISTA  
class Protagonista(Personaje):

    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, paciencia: int, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
        self.nivel = nivel
        [seleccionar_nuevo_ataque(0) for _ in range(4)]
        
    def seleccionar_subida_caracteristicas(self):
        característica_escogida = '0'
        while característica_escogida not in ['1', '2', '3', '4']:
            try:
                característica_escogida = input('''\nEscoge qué característica deseas incrementar:\n 
    - 1. Energia +10
    - 2. Empatía +5 
    - 3. Dialectica +5
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
            self.dialectica += 5    
            print(f'Has subido tu dialectica a {self.dialectica}\n')
        elif característica_escogida == '4':
            self.paciencia += 2
            print(f'Has subido tu paciencia a {self.paciencia}\n')

    def subir_nivel(self):
        self.nivel += 1
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
        
    def eleccion_ataque(self):
        print(f'Acciones disponibles:')
        print(f'\t- 1. Argumento razonable:')
        for i in AtaqueProta.arg_razonable:
            print(f'\t\t{i.nombre} (daño total: {i.daño * self.dialectica}, empatico: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})')
        print(f'\t- 2. Acción amistosa:')
        for i in AtaqueProta.acc_amistosa:
            print(f'\t\t{i.nombre} (daño total: {i.daño * self.dialectica}, empatico: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})')
        print(f'\t- 3. Ataque toxico:')
        for i in AtaqueProta.arg_toxico:
            print(f'\t\t{i.nombre} (daño total: {i.daño * self.dialectica}, empatico: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})')
        print(f'\t- 4. Argumento cutre:')
        for i in AtaqueProta.arg_cutre:
            print(f'\t\t{i.nombre} (daño total: {i.daño * self.dialectica}, empatico: {i.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})')

        ataque_elegido = '0'
        while ataque_elegido not in ['1', '2', '3', '4']:
            try: 
                ataque_elegido = input('Qué deseas realizar?: ')
            except ValueError:
                print('Debes escoger un número entre 1 y 4')

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

    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, enfado: int, paciencia: int, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
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
    
    def novia_enfadada(self):
        if self.enfado >= 100: 
            print('El nivel de enfado de la novia es demasiado alto. Tu novia te ha dejado. Game Over.')
            sys.exit()         
        
# CLASE HIJO ENEMIGO 
class Enemigo(Personaje):
    
    lista_ataques_enemigo = []
    
    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, enfado: int, paciencia: int, ataque_enemigo: str, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
        self.enfado = enfado
        self.ataque_enemigo = ataque_enemigo
        self.nivel = nivel

    def __str__(self):
        return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatia}, Dialectica: {self.dialectica}, Enfado: {self.enfado}, Ataque: {self.ataque_enemigo}, Paciencia: {self.paciencia}"
    
    def eleccion_ataque(self):
        print('Ataque Enemigo: ')
        print(f"{self.nombre} ataca con '{self.ataque_enemigo.nombre}' con una fuerza de {self.ataque_enemigo.daño * self.dialectica}")
        return self.ataque_enemigo
        
# ALIADO
class Aliado():

    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __str__(self):
        return f"Nombre: {self.nombre}"

    def eleccion_personaje(self, personaje, novia):
        # El Padre te da un consejo y te da una nueva habilidad
        if self.nombre == 'Padre':
            print(f'Tu padre te ofrece dos herramientas para mitigar el enfado de tu novia. ¿Cuál escoges?')
            seleccionar_nuevo_ataque(personaje.nivel)
            print('Tu padre te ha dado un par de consejos y te sientes más seguro de ti mismo')

        # La Madre te da un consejo y te sube una
        elif self.nombre == 'Madre':
            print('Tu madre te explica que no es bueno discutir con tu novia, es mejor hablar las cosas tranquilamente')
            personaje.seleccionar_subida_caracteristicas()
            print('Tu madre siempre es sabia y te sientes más seguro de ti mismo')

        # La Abuela te da de comer y te sube la energía y alguna característica
        elif self.nombre == 'Abuela':
            comida = input('''Tu abuela te pregunta que quieres para comer: 
                  
                - 1. Lentejas (+20 energia)
                - 2. Tortilla (+10 empatia, +10 energia)
                - 3. Macarrones (+10 dialectica, +10 energia)
                - 4. Pescado (+5 empatia, +5 dialectica)
                  
                  Tu respuesta: 
            ''')
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
        
        # El Abuelo te cuenta una historia y te sube de nivel pero te baja la empatía y sube el enfado de tu novia
        elif self.nombre == 'Abuelo':
            eleccion = input('''Tu abuelo te cuenta la historia de cuando era joven y tu abuela se enfadó muchísimo con él. 
                             Qué lástima que sean tiempos tan distintos... ¿Quieres seguir sus consejos?:
                             
                             - 1. Sí
                             - 2. No
                             
                             Tu respuesta:''')
            if eleccion == '1':
                personaje.empatia -= 10
                personaje.subir_nivel()
            elif eleccion == '2':
                print('Piensas que tu abuelo tiene ideas anticuadas y no le haces caso. Al menos te ha dado chuches.')
                personaje.energia += 10

        # El Amigo te da un consejo y te sube la dialectica
        elif self.nombre == 'Amigo':
            print('Tu amigo intenta darte un consejo pero no se le ocurre nada. Al menos te ha dado un Red Bull.')
            personaje.dialectica += 10

        # Tu amiga te invita a su casa a ver una peli y te sube la energía y la empatía pero sube el enfado de tu novia
        elif self.nombre == 'Amiga':
            eleccion = input('''Tu amiga quiere que te vayas a su casa a ver una peli para calmarte. ¿Aceptas?
                - 1. Sí
                - 2. No
                ''')
            if eleccion == '1':
                print('Veis Shreck y te sientes mucho más comprendido y con energía. Que pena que te vieron con tu amiga...')
                personaje.energia += 50
                personaje.paciencia += 2
                personaje.empatia -= 5
                novia.enfado += 10
            elif eleccion == '2':
                print('Tu amiga te dice que no te preocupes, que te va a ayudar a salir de esta')
                personaje.dialectica += 10
        
        # Tu hermano te invita a jugar al futbol o a tomar unas cervezas
        elif self.nombre == 'Hermano':
            eleccion = input('''Tu hermano te dice de hacer algo con él para que te distraigas. ¿Qué prefieres?
                             
                             - 1. Ir a jugar al futbol (-10 energía, +10 empatia)
                             - 2. Ir a tomar unas cervezas (+20 energia), -5 dialectica)''') 
  
            if eleccion == '1':
                print('El partida te ha cansado un poco pero te sientes más empático')
                personaje.energia -= 10
                personaje.empatia += 10
            elif eleccion == '2':
                print('Te sientes achispado pero te cuesta algo vocalizar tus argumentos')
                personaje.energia += 30
                personaje.dialectica -= 5
            
        # Tu hermana te invita a ir de compras o a un escape room
        elif self.nombre == 'Hermana':
            eleccion = input('''Tu hermana entiende perfectamente la situación y te da un abrazo. 
            Te ofrece un par de planes para desconectar:
                             
                             - 1. Ir de compras (-10 energia, +5 empatia, +5 dialectica)
                             - 2. Ir a un escape room (-20 energia, +3 paciencia)''')
            if eleccion == '1':
                print('Te sientes más carismático')
                personaje.energia -= 10
                personaje.empatia += 5
                personaje.dialectica += 5
            elif eleccion == '2':
                print('Te sientes más tranquilo')
                personaje.energia -= 20
                personaje.paciencia += 3
            
    
    
    