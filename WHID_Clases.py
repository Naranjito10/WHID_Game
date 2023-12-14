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
    
    def morir(self, contrincante):
        self.energia = 0
        if self.estado != sin_estado:
            self.estado.resetear_estadisticas()
        print(self.nombre, 'se ha quedado sin ENERGÍA para seguir discutiendo.')
        if self.__class__.__name__ == 'Protagonista':
            print('No eres capaz de seguir luchando por mantener a tu novia y huyes. Game Over')
            sys.exit()
        else: 
            contrincante.estado.resetear_estadisticas()
            

    def subir_caracteristicas_enemigo(self, nivel):
        self.energia += 10 * nivel
        self.dialectica += 1 * nivel
        self.paciencia += 1 * nivel
        
    # FUNCIONES ENFADO Y EMPATIA
    def ajustar_enfado_novia(self, ataque, novia, personaje):
        if not novia.novia_enfadada():
            if self.__class__.__name__ == 'Boss':
                enfado_total = ataque.empatia + personaje.empatia + (ataque.enfado * 3)
                self.enfado += enfado_total
            else:
                enfado_total = ataque.enfado
                novia.enfado += enfado_total

            if enfado_total > 0:
                print(f'El ENFADO de {novia.nombre} ha subido a {novia.enfado}')
            elif enfado_total < 0:
                print(f'El ENFADO de {novia.nombre} ha bajado a {novia.enfado}')
            else:
                print(f'El ENFADO de {novia.nombre} no ha cambiado ({novia.enfado})')
            
    
    def ajustar_empatia(self, ataque, personaje):
        if self.__class__.__name__ == 'Enemigo':
            empatia_total = ataque.empatia + personaje.empatia
            self.empatia_inicial += empatia_total
            if empatia_total > 0:
                print(f'La EMPATÍA de {self.nombre} ha subido a {self.empatia_inicial}')
            elif empatia_total < 0:
                print(f'La EMPATÍA de {self.nombre} ha bajado a {self.empatia_inicial}')
            else:
                print(f'La EMPATÍA de {self.nombre} no ha cambiado')

    def comprobar_empatia(self, novia):
        if self.empatia_inicial > 50:
            novia.enfado -= 10
            print(f'\n{self.nombre} le ha hablado a {novia.nombre} bien sobre ti y ha bajado su ENFADO a {novia.enfado}')
        elif self.empatia_inicial < -50:
            novia.enfado += 10
            print(f'\n{self.nombre} le ha hablado a {novia.nombre} sobre lo que le has dicho y ha subido su ENFADO a {novia.enfado}')

    # FUNCIONES ESTADO
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
            self.estado.resetear_estadisticas()
            self.estado = sin_estado  

    # FUNCIONES PELEA
    def daño_stun_estado(self):
        efecto_stun = False
        if self.estado.nombre != 'Sin estado':
            print(f'{self.nombre} está {self.estado.nombre}')
            if self.estado.probabilidad_trigger_estado() == False:
                print(f'{self.estado.nombre} no hizo efecto')
                return efecto_stun
            if self.estado.daño != 0:
                if self.estado.efecto == 'Veneno':
                    daño_efecto = self.estado.daño * self.estado.contador
                    self.energia -= daño_efecto
                else: 
                    daño_efecto = self.estado.daño
                    self.energia -= daño_efecto
                print(f'{self.nombre} ha recibido {daño_efecto} de daño por el estado {self.estado.nombre}. Ahora su ENERGÍA es {self.energia}')
                self.bajar_contador_estado()
            
            if self.estado.efecto == 'Stun': 
                print(f'\n{self.nombre} está ATURDIDO y no podrá atacar\n')    
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
            if self.__class__.__name__ == 'Protagonista':
                print(f'\n>>> {contrincante.nombre} argumenta con una FUERZA total (restando la PACIENCIA de {self.nombre}) de {daño_ataque_contrincante}.\n') 
            elif self.__class__.__name__ == 'Enemigo':
                empatia_total = ataque_contrincante.empatia + contrincante.empatia
                print(f'\n>>> {contrincante.nombre} argumenta con una FUERZA total (restando la PACIENCIA de {self.nombre}) de {daño_ataque_contrincante} y una EMPATÍA total de {empatia_total}.\n') 
                self.ajustar_empatia(ataque_contrincante, contrincante)
            elif self.__class__.__name__ == 'Boss':
                print(f'\n>>> {contrincante.nombre} argumenta con una FUERZA total (restando la PACIENCIA de {self.nombre}) de {daño_ataque_contrincante}.\n')        
            self.ajustar_enfado_novia(ataque_contrincante, novia, contrincante)
            # APLICAR ESTADO
            self.aplicar_estado(ataque_contrincante)
            # BAJAR VIDA
            self.energia = self.energia - daño_ataque_contrincante
            print(f'\nA {self.nombre} le baja la ENERGÍA a {self.energia}.\n')
            if self.esta_vivo() == False: 
                self.morir(contrincante)

    def calcular_daño(self, contrincante, ataque_contrincante):
        daño = ataque_contrincante.daño * contrincante.dialectica 
        paciencia_anulada = 0
        # print(f'\n----- ESTADO DEL DEFENSOR: -----\n')
        if self.estado.nombre != 'Sin estado':
            print(f'El estado de {self.nombre} es {self.estado.nombre}')
            # print(f'{self.nombre} está {self.estado.nombre}')
            if self.estado.probabilidad_trigger_estado == False:
                # print(f'{self.estado.nombre} no hizo efecto para este ataque')
                pass
            
            else:
                if self.estado.efecto == 'Bajar armadura':
                    paciencia_anulada = self.paciencia
                    print(f'{self.nombre} ha perdido toda su PACIENCIA para defenderse por el efecto {self.estado.efecto}\n')
                    self.bajar_contador_estado()
                else: 
                    # print(f'El estado {self.estado.nombre} tiene el efecto {self.estado.efecto} pero ahora no hace nada a {self.nombre}')
                    pass

        if contrincante.estado.efecto == 'Reducir daño':
            print(f'\nEl estado de {contrincante.nombre} es {contrincante.estado.nombre} con el efecto {contrincante.estado.efecto}')
            print(f'De este modo el daño del siguiente ataque de {contrincante.nombre} se reduce a la mitad')
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
        experiencia_requerida = self.calcular_experiencia_siguiente_nivel(dificultad)
        sobrante_experiencia = experiencia_requerida - self.experiencia
        if self.nivel == 0:
            print('''\nConceptos básicos:\n
    - La "ENERGÍA" es la capacidad de aguante. Te permite aguantar más argumentos.
    - La "DIALÉCTICA" es la fuerza de tus argumentos. Cuanto más alta sea, más fácil será bajar la ENERGÍA de tus contrincantes.
    - La "EMPATÍA" es la capacidad de ponerte en el lugar de la otra persona. Una persona empática siempre cae mejor.
    - La "PACIENCIA" es la capacidad de reducir el peso de un argumento. Determina cuanto te afectarán los argumentos.
    - El "ENFADO" de tu novia no puede llegar a 100, sino te dejará y tus suegros montarán una fiesta.
    - Llamaremos a los puntos de experiencia "Puntos de Amor" o "PA"\n''')
            sobrante_experiencia = 0
            self.subir_nivel(sobrante_experiencia)
            print(f'\nTe faltan {experiencia_requerida} PA para subir al siguiente nivel.\n')
            
        else:
            print(f'¡Has conseguido {cantidad} PA!')
            print(f'\nAhora tienes {self.experiencia} PA.')
            if sobrante_experiencia > 0:
                print(f'Te faltan {sobrante_experiencia} PA para subir al siguiente nivel.\n')
            else:
                print('Tienes suficientes PA para subir de nivel.\n')
                while self.experiencia >= experiencia_requerida:
                    self.subir_nivel(sobrante_experiencia)
        
    def subir_nivel(self, sobrante_experiencia):
        self.nivel += 1
        self.experiencia = sobrante_experiencia
        if self.nivel == 1:
            print(f'\nAhora eres nivel {self.nivel}.')
            self.seleccionar_subida_caracteristicas()
            print(f'\nTus características son: ')
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
        return 25 * (self.nivel + dificultad)

    def seleccionar_subida_caracteristicas(self):
        característica_escogida = '0'
        while característica_escogida not in ['1', '2', '3', '4']:
            try:
                característica_escogida = input('''\nEscoge qué característica deseas incrementar:\n 
    - 1. Energía +25
    - 2. Empatía +5 
    - 3. Dialéctica +3
    - 4. Paciencia +2
                \nTu respuesta: ''')
            except ValueError:
                print('Debes escoger un número entre 1 y 4')

        if característica_escogida == '1':
            self.energia += 25
            print(f'Has subido tu ENERGÍA a {self.energia}\n')
        elif característica_escogida == '2':
            self.empatia += 5
            print(f'Has subido tu EMPATÍA a {self.empatia}\n')
        elif característica_escogida == '3':
            self.dialectica += 3  
            print(f'Has subido tu dialéctica a {self.dialectica}\n')
        elif característica_escogida == '4':
            self.paciencia += 2
            print(f'Has subido tu PACIENCIA a {self.paciencia}\n')
      
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
        
        categoria_elegida = []
        while categoria_elegida == []:

            if ataque_elegido == '1' and len(AtaqueProta.arg_razonable) == 0:
                print('No tienes argumentos razonables disponibles, escoge otra opción')
            elif ataque_elegido == '2' and len(AtaqueProta.acc_amistosa) == 0:
                print('No tienes acciones amistosas disponibles, escoge otra opción')
            elif ataque_elegido == '3' and len(AtaqueProta.arg_toxico) == 0:
                print('No tienes argumentos tóxicos disponibles, escoge otra opción')
            elif ataque_elegido == '4' and len(AtaqueProta.arg_cutre) == 0:
                print('No tienes argumentos cutres disponibles, escoge otra opción')   

            elif ataque_elegido == '1' and len(AtaqueProta.arg_razonable) != 0: 
                categoria_elegida = AtaqueProta.arg_razonable
            elif ataque_elegido == '2' and len(AtaqueProta.acc_amistosa) != 0:
                categoria_elegida = AtaqueProta.acc_amistosa
            elif ataque_elegido == '3' and len(AtaqueProta.arg_toxico) != 0:
                categoria_elegida = AtaqueProta.arg_toxico
            elif ataque_elegido == '4' and len(AtaqueProta.arg_cutre) != 0:
                categoria_elegida = AtaqueProta.arg_cutre

        ataque_random = random.choice(categoria_elegida)
        print(f'\n>>> {self.nombre} ataca con {ataque_random.nombre} con una fuerza de {ataque_random.daño * self.dialectica} y posibilidad de afectar con el estado {ataque_random.estado.nombre}')
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
        return f'Nombre: {self.nombre}, Energía: {self.energia}, Dialéctica: {self.dialectica}, Enfado: {self.enfado}, Paciencia: {self.paciencia}'

    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'\nAhora el Boss es nivel {self.nivel}')
        else: 
            print(f'\nAhora el Boss es nivel {self.nivel}')

        seleccionar_nuevo_ataque_boss(self.nivel)
    
    def eleccion_ataque(self):
        ataque_random = random.choice(AtaqueBoss.lista_ataques_boss)
        print('- - - Ataque Boss - - -')
        print(f'\n>>> {self.nombre} ataca con {ataque_random.nombre} con una fuerza de {ataque_random.daño * self.dialectica} y posibilidad de afectar con el estado {ataque_random.estado.nombre}')
        return ataque_random
    
    def novia_enfadada(self):
        if self.enfado >= 100: 
            print('El nivel de enfado de la novia es demasiado alto. Tu novia te ha dejado. Game Over.')
            sys.exit()         
        
# CLASE HIJO ENEMIGO 
class Enemigo(Personaje):
    
    lista_ataques_enemigo = []
    
    def __init__(self, nombre: str, energia: int, empatia: int, empatia_inicial: int, dialectica: int, paciencia: int, ataque_enemigo: str, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
        self.empatia_inicial = empatia_inicial
        self.ataque_enemigo = ataque_enemigo
        self.nivel = nivel
        self.establecer_caracteristicas_nivel(self.nivel)

    def __str__(self):
        return f'Nombre: {self.nombre}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}, Ataque: {self.ataque_enemigo}, Paciencia: {self.paciencia}'
    
    def establecer_caracteristicas_nivel(self, nivel):
        self.subir_caracteristicas_enemigo(nivel)
        self.empatia_inicial = self.empatia_inicial - (3 * nivel)

    def eleccion_ataque(self):
        print(f'\n>>> {self.nombre} ataca con {self.ataque_enemigo.nombre} con una fuerza de {self.ataque_enemigo.daño * self.dialectica} y posibilidad de afectar con el estado {self.ataque_enemigo.estado.nombre}')
        return self.ataque_enemigo


                
    
    