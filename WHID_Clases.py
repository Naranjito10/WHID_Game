import random
from WHID_Ataques import *
import math
import sys

# PERSONAJE
class Personaje: 

    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, paciencia: int, estado = sin_estado):
        self.nombre = nombre
        self.energia = energia
        self.energia_maxima = energia
        self.energia_actual = ''
        self.empatia = empatia
        self.dialectica = dialectica
        self.paciencia = paciencia
        self.estado = estado
    
    # FUNCIONES VIDA
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
            contrincante.estado = sin_estado
            
    def print_energia_actual(self):
        self.energia_actual = f'{self.energia}/{self.energia_maxima}'
        return self.energia_actual
    
    def bajar_vida(self, daño):
        self.energia = self.energia - daño

    def curar_vida(self, cura):
        self.energia = self.energia + cura
        if self.energia > self.energia_maxima:
            self.energia = self.energia_maxima

    def cura_maxima(self):
        self.energia = self.energia_maxima
        if self.__class__.__name__ == 'Protagonista' and self.nivel != 1:
            print(f'\n{self.nombre} se ha curado al máximo al subir de nivel.')

    def subir_vida_maxima(self, vida):
        self.energia_maxima = self.energia_maxima + vida

    def subir_caracteristicas_enemigo(self, nivel):
        self.energia_maxima += 20 * nivel
        self.cura_maxima()
        self.dialectica += 1 * nivel
        self.paciencia += 1 * nivel
        
    # FUNCIONES ENFADO Y EMPATIA
    def ajustar_enfado_novia(self, ataque, novia, personaje):
        if not novia.novia_enfadada():
            if self.__class__.__name__ == 'Boss':
                enfado_total = (ataque.enfado * 3) - ataque.empatia//2 - personaje.empatia//3
                self.enfado += enfado_total
                self.enfado = max(0, self.enfado)
            else:
                enfado_total = ataque.enfado
                novia.enfado += enfado_total
                novia.enfado = max(0, novia.enfado)

            print('\n___________________ ENFADO NOVIA ___________________________')
            if enfado_total > 0:
                print(f'\nEl ENFADO de {novia.nombre} ha subido a {novia.enfado}')
            elif enfado_total < 0:
                print(f'\nEl ENFADO de {novia.nombre} ha bajado a {novia.enfado}')
            else:
                print(f'\nEl ENFADO de {novia.nombre} no ha cambiado ({novia.enfado})')
             
    def ajustar_empatia(self, ataque, personaje):
        empatia_total = ataque.empatia + personaje.empatia
        self.empatia_inicial += empatia_total

        if empatia_total > 0:
            print(f'La EMPATÍA de {self.nombre} ha subido a {self.empatia_inicial}')
        elif empatia_total < 0:
            print(f'La EMPATÍA de {self.nombre} ha bajado a {self.empatia_inicial}')
        else:
            print(f'La EMPATÍA de {self.nombre} no ha cambiado')

    def comprobar_empatia(self, novia, prota):
        if self.empatia_inicial >= 50 and self.empatia_inicial < 100:
            novia.enfado -= 10
            novia.enfado = max(0, novia.enfado)
            print(f'\n{self.nombre} le ha hablado a {novia.nombre} bien sobre ti y ha bajado su ENFADO a {novia.enfado}')

        elif self.empatia_inicial >= 100:
            novia.enfado -= 20
            novia.enfado = max(0, novia.enfado)
            print(f'\n{self.nombre} le ha hablado a {novia.nombre} muy bien sobre ti y ha bajado su ENFADO a {novia.enfado}')
            print(f'Además, sientes que tienes una nueva amistad, lo que te reconforta.')
            prota.seleccionar_subida_caracteristicas()

        elif self.empatia_inicial <= -50 and self.empatia_inicial > -100:
            novia.enfado += 10
            print(f'\n{self.nombre} le ha hablado a {novia.nombre} sobre lo que le has dicho y ha subido su ENFADO a {novia.enfado}')

        elif self.empatia_inicial <= -100:
            novia.enfado += 20
            print(f'\n{self.nombre} le ha hablado a {novia.nombre} muy mal sobre ti y ha subido su ENFADO a {novia.enfado}')
            print(f'Además, sientes que tu novia no te lo perdonará...')
            novia.subir_nivel()
        
    # FUNCIONES ESTADO
    def comprobar_afectar_estado(self, ataque):

        if ataque.estado != sin_estado:
            estado_afecta = ataque.estado.probabilidad_afectar_estado()
            sin_estado_y_afecta = self.estado == sin_estado and estado_afecta
            con_estado_y_afecta = self.estado != sin_estado and estado_afecta
            sin_estado_no_afecta = self.estado == sin_estado and not estado_afecta
            con_estado_no_afecta = self.estado != sin_estado and not estado_afecta

            if sin_estado_y_afecta:
                self.estado = ataque.estado
                print(f'{self.nombre} no tenía estado y ahora tiene el estado {ataque.estado.nombre} con un contador de {self.estado.contador}')

            elif con_estado_y_afecta:
                if ataque.estado.nombre == self.estado.nombre: 
                    self.estado.subir_contador()
                    print(f'{self.nombre} ha incrementado su estado {ataque.estado.nombre} a {self.estado.contador}') 
                else: 
                    print(f'{self.nombre} reemplaza su estado {self.estado.nombre}')
                    self.estado = ataque.estado
                    print(f'Ahora tiene el estado {ataque.estado.nombre}')

            elif sin_estado_no_afecta:
                print(f'\n{self.nombre} no tiene ningún estado y no ha recibido el estado {ataque.estado.nombre}')

            elif con_estado_no_afecta:
                print(f'{self.nombre} tiene estado el estado {self.estado.nombre} y no ha sido afectado por el nuevo estado {ataque.estado.nombre}')
        
    def bajar_contador_estado(self):
        self.estado.contador -= 1
        print(f'El contador del estado ha bajado a {self.estado.contador}')
        if self.estado.contador == 0:
            print(f'{self.nombre} ya no tiene el estado {self.estado.nombre}\n')
            self.estado.resetear_estadisticas()
            self.estado = sin_estado  

    def ataque_estado_propio(self, ataque, enemigo):
            if ataque.estado.efecto in ['Reducir daño', 'Stun', 'Veneno', 'Sofocado', 'Ataque no afecta', 'Efecto no afecta']:
                print(f'\n>>> {self.nombre} ataca con {ataque.nombre} con una fuerza de {ataque.daño * self.dialectica} y posibilidad de afectar con el estado {ataque.estado.nombre} a {enemigo.nombre}.')
            elif ataque.estado.efecto in ['Dobla Ataque', 'Cura ataque']:
                print(f'\n>>> {self.nombre} ataca con {ataque.nombre} con una fuerza de {ataque.daño * self.dialectica}.')
                self.comprobar_afectar_estado()
            elif ataque.estado.efecto == 'Sin estado':
                pass

    # FUNCIONES PELEA
    def daño_stun_estado(self):
        efecto_stun = False
        con_estado = self.estado.nombre != 'Sin estado'
        no_trigger = self.estado.probabilidad_trigger_estado() == False
        estado_hace_daño = self.estado.daño != 0
        if con_estado:
            print(f'{self.nombre} está {self.estado.nombre}')

            if no_trigger:
                print(f'{self.estado.nombre} no hizo efecto')
                return efecto_stun
            
            if estado_hace_daño:
                if self.estado.efecto == 'Veneno':
                    daño_efecto = self.estado.daño * self.estado.contador
                    self.bajar_vida(daño_efecto)

                else: 
                    daño_efecto = self.estado.daño
                    self.bajar_vida(daño_efecto)

                print(f'{self.nombre} ha recibido {daño_efecto} de daño por el estado {self.estado.nombre}. Ahora su ENERGÍA es {self.energia}')
                self.bajar_contador_estado()
            
            if self.estado.efecto == 'Stun': 
                print(f'\n{self.nombre} está ATURDIDO y no podrá atacar\n')    
                efecto_stun = True
                self.bajar_contador_estado()
                return efecto_stun
        
        return efecto_stun
            
    def defender(self, contrincante, novia): 
        contrincante_no_stuneado = contrincante.daño_stun_estado() == False
        if contrincante_no_stuneado:
            ataque_contrincante = contrincante.eleccion_ataque(self)
            daño_ataque_contrincante = self.calcular_daño(contrincante, ataque_contrincante)
            if self.__class__.__name__ == 'Protagonista':
                print(f'\n>>> {contrincante.nombre} argumenta con una FUERZA total (restando la PACIENCIA de {self.nombre}) de {daño_ataque_contrincante}.\n') 
            elif self.__class__.__name__ == 'Enemigo':
                empatia_total = ataque_contrincante.empatia + contrincante.empatia
                print(f'\n>>> {contrincante.nombre} argumenta con una FUERZA total (restando la PACIENCIA de {self.nombre}) de {daño_ataque_contrincante} y una EMPATÍA total de {empatia_total}.\n') 
                self.ajustar_empatia(ataque_contrincante, contrincante)
            elif self.__class__.__name__ == 'Boss':
                print(f'\n>>> {contrincante.nombre} argumenta con una FUERZA total (restando la PACIENCIA de {self.nombre}) de {daño_ataque_contrincante}.\n')
            if contrincante.estado.efecto == 'Cura ataque':
                mitad_daño = daño_ataque_contrincante // 2
                contrincante.energia += mitad_daño
                print(f'{contrincante.nombre} se cura {mitad_daño} puntos de energía y sube a {contrincante.print_energia_actual()}.\n')       
            self.bajar_vida(daño_ataque_contrincante)
            print(f'\nA {self.nombre} le baja la ENERGÍA a {self.print_energia_actual()}.\n')
            self.comprobar_afectar_estado(ataque_contrincante)
            self.ajustar_enfado_novia(ataque_contrincante, novia, contrincante)
            if self.esta_vivo() == False: 
                self.morir(contrincante)

    def calcular_daño(self, contrincante, ataque_contrincante):
        daño = ataque_contrincante.daño * contrincante.dialectica 
        if contrincante.__class__.__name__ == 'boss':
            daño = daño + contrincante.enfado // 3
        paciencia_anulada = 0
        si_trigger = self.estado.probabilidad_trigger_estado == True
        con_estado = self.estado.nombre != 'Sin estado'
        if con_estado:
            print(f'El estado de {self.nombre} es {self.estado.nombre}.\n')
            if si_trigger:
                if self.estado.efecto == 'Bajar armadura':
                    paciencia_anulada = self.paciencia
                    print(f'{self.nombre} ha perdido toda su PACIENCIA para defenderse por el efecto {self.estado.efecto}.\n')
                    self.bajar_contador_estado()
        
        if contrincante.estado.efecto == 'Efecto no afecta':
            print(f'{contrincante.nombre} está silenciado y no aplica ningún estado.\n')

        if contrincante.estado.efecto == 'Dobla ataque':
            daño = daño * 2
            
        # TODO Debería ser antes o después la reducción de la paciencia que del estado reducir daño? Creo que así está bien
        if daño >= self.paciencia:
            daño = daño - self.paciencia + paciencia_anulada
        else:
            daño = 0 

        if contrincante.estado.efecto == 'Reducir daño':
            print(f'El estado de {contrincante.nombre} es {contrincante.estado.nombre} con el efecto {contrincante.estado.efecto}.')
            print(f'De este modo el daño del siguiente ataque de {contrincante.nombre} se reduce a la mitad.\n')
            daño = math.floor(daño * 0.5)
            contrincante.bajar_contador_estado()

        return daño

# CLASE HIJO PROTAGONISTA  
class Protagonista(Personaje):

    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, paciencia: int, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
        self.nivel = nivel
        self.experiencia = 0
        [seleccionar_nuevo_ataque(0) for _ in range(4)]
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Nivel: {self.nivel}, Energía: {self.print_energia_actual()}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}, Paciencia: {self.paciencia}'
    
    def ganar_experiencia(self, cantidad, dificultad):
        experiencia_requerida = self.calcular_experiencia_siguiente_nivel(dificultad)
        self.experiencia += cantidad
        sobrante_experiencia = experiencia_requerida - self.experiencia
        # TODO comprobar si aquí llega con el nivel 0 porque creo que no
        if self.nivel == 0:
            self.subir_nivel()
            print(f'\nTe faltan {experiencia_requerida} PA para subir al siguiente nivel.\n') 
        else:
            print(f'\nHas conseguido {cantidad} PA!')
            print(f'\nAhora tienes {self.experiencia}/{experiencia_requerida} PA.')
            if self.experiencia < experiencia_requerida:
                print(f'Te faltan {sobrante_experiencia} PA para subir al siguiente nivel.\n')
            else:
                print('Tienes suficientes PA para subir de nivel.\n')
                sobrante_experiencia = abs(sobrante_experiencia)
                while self.experiencia >= experiencia_requerida:
                    self.experiencia = self.experiencia - experiencia_requerida
                    self.subir_nivel()
        
    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'\nAhora eres nivel {self.nivel}.')
        else: 
            print(f'\nAcabas de subir al nivel {self.nivel}')
        self.seleccionar_subida_caracteristicas()
        self.cura_maxima()
        print(f'\nAhora tus características son: ')
        print(self)
        print(f'\nEscoge entre estas dos habilidades para añadir a tu kit de habilidades: ')
        seleccionar_nuevo_ataque(self.nivel)

    def calcular_experiencia_siguiente_nivel(self, dificultad):
        return 40 * (self.nivel + dificultad)

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
            self.energia_maxima += 25
            print(f'Has subido tu ENERGÍA MÁXIMA a {self.energia_maxima}\n')
        elif característica_escogida == '2':
            self.empatia += 5
            print(f'Has subido tu EMPATÍA a {self.empatia}\n')
        elif característica_escogida == '3':
            self.dialectica += 3  
            print(f'Has subido tu DIALÉCTICA a {self.dialectica}\n')
        elif característica_escogida == '4':
            self.paciencia += 2
            print(f'Has subido tu PACIENCIA a {self.paciencia}\n')

        continuar()

    def eleccion_ataque(self, enemigo):
        print(f'\n----- ATAQUE DE {self.nombre} -----\n')
        print(f'Acciones disponibles:\n')
        if self.estado.efecto == 'Solo toxicos':
            print(f'¡Atención! Como tienes el estado {self.estado.nombre}, solo puedes atacar con ataques tóxicos.\n')
        elif self.estado.efecto == 'Solo razonables':
            print(f'¡Atención! Como tienes el estado {self.estado.nombre}, solo puedes atacar con ataques razonables.\n')

        tipos_ataque = [
            ("1. Argumento razonable", AtaqueProta.arg_razonable),
            ("2. Acción amistosa", AtaqueProta.acc_amistosa),
            ("3. Ataque tóxico", AtaqueProta.arg_toxico),
            ("4. Argumento cutre", AtaqueProta.arg_cutre)
            ]
        
        if enemigo.__class__.__name__ == 'Enemigo':
            for tipo, lista_ataque in tipos_ataque:
                print(f'\t- {tipo}:')
                for i in lista_ataque:
                    print(f'\t\t{i.nombre}')
                    print(f'\t\t(Daño total: {i.daño * self.dialectica}, empatía: {i.empatia + self.empatia}, enfado a la novia: {i.enfado}, estado: {i.estado.nombre})\n')
        
        elif enemigo.__class__.__name__ == 'Boss':
            for tipo, lista_ataque in tipos_ataque:
                print(f'\t- {tipo}:')
                for i in lista_ataque:
                    print(f'\t\t{i.nombre}')
                    print(f'\t\t(Daño total: {i.daño * self.dialectica}, enfado a la novia: {i.enfado*3 - i.empatia//2 - self.empatia//3}, estado: {i.estado.nombre})\n')
        
        categoria_elegida = []

        while categoria_elegida == []:
            ataque_elegido = '0'

            if self.estado.efecto == 'Solo toxicos':
                while ataque_elegido not in ['3', '4']:
                    try: 
                        ataque_elegido = input('¿Qué deseas realizar?: ')
                    except ValueError:
                        print(f'\nComo tienes el estado {self.estado.nombre}, solo puedes atacar con ataques tóxicos. Debes escoger un número entre el 3 y el 4')

            elif self.estado.efecto == 'Solo razonables':
                print(f'Como tienes el estado {self.estado.nombre}, solo puedes atacar con ataques razonables')
                while ataque_elegido not in ['1', '2']:
                    try: 
                        ataque_elegido = input('¿Qué deseas realizar?: ')
                    except ValueError:
                        print(f'\nComo tienes el estado {self.estado.nombre}, solo puedes atacar con ataques tóxicos. Debes escoger un número entre el 1 y el 2')
            else: 
                while ataque_elegido not in ['1', '2', '3', '4']:
                    try: 
                        ataque_elegido = input('¿Qué deseas realizar?: ')
                    except ValueError:
                        print('\nDebes escoger un número entre 1 y 4')

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
        continuar()
        self.ataque_estado_propio(ataque_random, enemigo)

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
    
    motivo_real = ''
    lista_descartados = []

    def __init__(self, nombre: str, energia: int, empatia: int, dialectica: int, enfado: int, paciencia: int, nivel: int, estado = sin_estado):
        super().__init__(nombre, energia, empatia, dialectica, paciencia, estado)
        self.enfado = enfado
        self.nivel = nivel
        [seleccionar_nuevo_ataque_boss(self.nivel) for _ in range(4)]

    def __str__(self):
        return f'Nombre: {self.nombre}, Energía: {self.print_energia_actual()}, Dialéctica: {self.dialectica}, Enfado: {self.enfado}, Paciencia: {self.paciencia}'
    
    # SELECCIÓN VEREDICTO
    def seleccionar_motivo_y_elementos(self, dificultad):
        Boss.motivo_real = random.choice(Boss.lista_motivos)
        # print(f'\nEl motivo seleccionado es: {Boss.motivo_real}')

        if dificultad == 1:
            seleccion_dificultad = 1
        elif dificultad == 2:
            seleccion_dificultad = 3
        elif dificultad == 3:
            seleccion_dificultad = 5 
        elif dificultad == 4:
            seleccion_dificultad = 7

        # Seleccionar x elementos aleatorios de la lista_motivos, excluyendo el motivo seleccionado
        elementos_seleccionados = random.sample([motivo for motivo in Boss.lista_motivos if motivo != Boss.motivo_real], seleccion_dificultad)

        # Agregar el motivo seleccionado a la lista final
        lista_final = [Boss.motivo_real] + elementos_seleccionados

        return lista_final
    
    def seleccion_motivos(self, lista_posibles_motivos):
        lista_motivos_restantes = []
        continuar()
        random.shuffle(lista_posibles_motivos)
        for motivo in lista_posibles_motivos:
            if motivo not in Boss.lista_descartados:
                lista_motivos_restantes.append(motivo)
        print(f'\nEl Boss está enfadado porque: {Boss.motivo_real}')
        print('\n¿Cuál crees que es la razón por la cual tu novia está enfadada?')
        print('\nEstas son las posibles razones: \n')
                
        for index, motivo in enumerate(lista_motivos_restantes, start=1):
            print(f'{index}: {motivo}')
            
        respuesta = ''
        longitud_lista = len(lista_motivos_restantes) + 1
        while respuesta not in range(longitud_lista):
            try:
                respuesta = int(input('\nSelecciona el motivo: '))
            except ValueError:
                print(f'Debes escoger un número entre 1 y {longitud_lista - 1}\n')
        
        seleccion = lista_motivos_restantes[respuesta - 1]
        print(f'\nHas seleccionado: {seleccion}')
        if Boss.motivo_real == seleccion:
            return True
        else:
            Boss.lista_descartados.append(seleccion)
            return False       

    # Subir nivel
    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'\nAhora el Boss es nivel {self.nivel}')
        else: 
            print(f'\nAhora el Boss es nivel {self.nivel}')
        self.subir_caracteristicas_enemigo(self.nivel)
        seleccionar_nuevo_ataque_boss(self.nivel)
    
    def eleccion_ataque(self, enemigo):
        ataque_random = random.choice(AtaqueBoss.lista_ataques_boss)
        print('- - - Ataque Boss - - -')
        self.ataque_estado_propio(ataque_random, enemigo)
        return ataque_random
    
    def novia_enfadada(self):
        if self.enfado >= 100: 
            print('El nivel de enfado de la novia es demasiado alto. Tu novia te ha dejado. Game Over.')
            sys.exit()      
        elif self.enfado < 0:
            self.enfado = 0 
        
        
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
        return f'Nombre: {self.nombre}, Energía: {self.print_energia_actual()}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}, Ataque: {self.ataque_enemigo.nombre}, Paciencia: {self.paciencia}'
    
    def establecer_caracteristicas_nivel(self, nivel):
        self.subir_caracteristicas_enemigo(nivel)
        self.empatia_inicial = self.empatia_inicial - (3 * nivel)

    def eleccion_ataque(self, enemigo):
        self.ataque_estado_propio(self.ataque_enemigo, enemigo)
        return self.ataque_enemigo


                
    
    