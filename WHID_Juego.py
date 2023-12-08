from WHID_Clases import *
from WHID_Ataques import *
from random import randint
import sys

# FUNCIONES

# SELECCIÓN DE DIFICULTAD
def personajes_segun_dificultad(dificultad):
    # CREACIÓN DE BOSS
    if dificultad == 1:
        dificultad_boss = 0
        dificultad_enemigos = 0
    elif dificultad == 2:
        dificultad_boss = 0
        dificultad_enemigos = 1
    elif dificultad == 3:
        dificultad_boss = 1
        dificultad_enemigos = 1
    elif dificultad == 4:
        dificultad_boss = 2
        dificultad_enemigos = 2

    # CREACIÓN BOSS
    novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, paciencia = 1, nivel = dificultad_boss)
    
    # CREACIÓN DE NPC ENEMIGOS

    ataque_suegro = AtaqueEnemigo(nombre = '"No vales tanto como para estar con ella"', daño = 0.5, nivel = 0, enfado = 0, estado = quemado, empatia = 0)
    suegro = Enemigo(nombre = 'Suegro', energia = 40, empatia = 0, dialectica = 5, enfado = 50, paciencia = 1, ataque_enemigo = ataque_suegro, nivel = dificultad_enemigos, estado = sin_estado)

    ataque_suegra = AtaqueEnemigo(nombre = '"¿Aún no te ha dejado?"', daño = 0.5,  nivel = 0, enfado = 0, estado = quemado, empatia = 0)
    suegra = Enemigo(nombre = 'Suegra', energia = 40, empatia = 0, dialectica = 5, enfado = 50, paciencia = 1, ataque_enemigo = ataque_suegra, nivel = dificultad_enemigos, estado = sin_estado)

    ataque_cuñado = AtaqueEnemigo(nombre = '"No sé de qué me hablas. Seguro que le has puesto los cuernos..."', daño = 5,  nivel = 0, enfado = 0, estado = paralizado, empatia = 0)
    cuñado = Enemigo(nombre = 'Cuñado', energia = 40, empatia = 0, dialectica = 5, enfado = 50, paciencia = 0, ataque_enemigo = ataque_cuñado, nivel = dificultad_enemigos, estado = sin_estado)

    ataque_cuñada = AtaqueEnemigo(nombre = '"Eres un inútil."', daño = 0.5, nivel = 0, enfado = 0, estado = paralizado, empatia = 0)
    cuñada = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, paciencia = 0, ataque_enemigo = ataque_cuñada, nivel = dificultad_enemigos, estado = sin_estado)
    
    ataque_cuñada = AtaqueEnemigo(nombre = '"Eres un inútil."', daño = 0.5, nivel = 0, enfado = 0, estado = paralizado, empatia = 0)
    amigo_novia = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, paciencia = 0, ataque_enemigo = ataque_cuñada, nivel = dificultad_enemigos, estado = sin_estado)

    ataque_cuñada = AtaqueEnemigo(nombre = '"Eres un inútil."', daño = 0.5, nivel = 0, enfado = 0, estado = paralizado, empatia = 0)
    amiga_novia = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, paciencia = 0, ataque_enemigo = ataque_cuñada, nivel = dificultad_enemigos, estado = sin_estado)

    return novia, suegro, suegra, cuñado, cuñada, amigo_novia, amiga_novia

def seleccion_dificultad():
    respuesta = ''
    while respuesta not in [1, 2, 3, 4]: 
        respuesta = int(input('''Selecciona la dificultad: 
                          
        1: Nivel Fácil: Tu cagada no es tan grave y los enemigos y la novia te tienen algo de respeto
        2: Nivel Normal: Tu cagada es grave y los enemigos y la novia te tienen poco respeto
        3: Nivel Difícil: Tu cagada es muy grave y los enemigos y la novia son secos y agresivos contigo
        4: Nivel Realista: Tu cagada es tan grave que no tiene solución y tu novia está a punto de dejarte
                          
        Tu respuesta: '''))
    return respuesta

# SELECCIÓN VEREDICTO
def seleccion_motivos(novia, motivo, seleccion_dificultad):
    lista_descartados = []
    if seleccion_dificultad == 'Fácil':
        dificultad = 2
    elif seleccion_dificultad == 'Normal':
        dificultad = 4
    elif seleccion_dificultad == 'Difícil':
        dificultad = 6  
    elif seleccion_dificultad == 'Realista':
        dificultad = 8

    print('¿Cuál crees que es la razón por la cual tu novia está enfadada?')
    lista_posibles_motivos = random.sample(novia.lista_motivos, min(dificultad, len(novia.lista_motivos)))
    for i in lista_posibles_motivos if i not in lista_descartados else novia.lista_motivos:
        index, palabra = enumerate(i)
        print(f'{index}: {palabra}')
    respuesta = int(input('Selecciona el motivo: '))
    if respuesta == novia.lista_motivos.index(motivo):
        return True
    else:
        lista_descartados.append(novia.lista_motivos.index(motivo))
        return False       

# ENCUENTROS CON BOSS
def encuentro_boss(prota, novia, rondas, motivo, dificultad):
    print('\nTe encuentras con el BOSS FINAL: Tu novia. \nTiene estas características: ')
    print(novia)
    print('\nEstá esperando una respuesta por tu parte:')
    pelea_enemigo(prota, novia, novia)
    print('Muy bien, la has calmado.')
    novia.subir_nivel()
    prota.subir_nivel()
    if seleccion_motivos(novia, motivo, dificultad):
        print('Has conseguido adivinar el motivo del enfado. Has ganado.')
        print('Tu novia ahora sigue enfadada pero almenos sabe el porqué. ¿Has ganado?')
        sys.exit()
    else:
        rondas += 1
        if rondas == 5:
            print('Has terminado el juego. Has perdido.')
            sys.exit()
        else:
            print('El veredicto ha sido negativo. Debes seguir investigando.')
# CREADOR EVENTOS
def crear_eventos(lista_npc_totales, lista_aliados, lista_enemigos, dificultad):
    
    # AÑADIR NPC ENEMIGO ALEATORIOS
    for i in range(dificultad + 2):
        i = random.choice(lista_enemigos) if i not in lista_npc_totales else lista_enemigos
        lista_npc_totales.append(i)

    # AÑADIR NPC ALIADO ALEATORIOS
    cuenta_atras = [5, 4, 3, 2, 1]
    print(cuenta_atras[dificultad])

    for i in range(cuenta_atras[dificultad]):
        i = random.choice(lista_aliados) if i not in lista_npc_totales else lista_aliados
        lista_npc_totales.append(i)
        
# EVENTOS ALEATORIOS
def evento_aleatorio(lista_npc_totales, prota, novia):
    personaje_aleatorio = random.choice(lista_npc_totales)
    print(f'Te encuentras con la siguiente persona: {personaje_aleatorio.nombre}\n')
    if personaje_aleatorio in lista_npc_enemigos: 
        print(f'Debes interactuar con {personaje_aleatorio.nombre}. ¿Qué haces?\n')
        pelea_enemigo(prota, personaje_aleatorio, novia)
        prota.subir_nivel()
    else:
        personaje_aleatorio.eleccion_personaje(prota, novia)
    lista_npc_totales.remove(personaje_aleatorio)


# SISTEMA DE COMBATE
def informacion_batalla(prota, enemigo, novia, turno):
    print(f'La energía de {prota.nombre} es ***{prota.energia}***')
    print(f'\nLa energía de {enemigo.nombre} es ***{enemigo.energia}***')
    if turno == 0 and enemigo.__class__.__name__ == 'Boss':
        print(f'El enfado de tu novia {novia.nombre} es de ***{novia.enfado}***. Evita que llegue a 100')
        print(f'Con tu novia la empatía afecta directamente a su enfado. Ten cuidado.')

    elif turno != 0 and enemigo.__class__.__name__ == 'Boss':
        print(f'El enfado de tu novia {novia.nombre} es de ***{novia.enfado}***. Evita que llegue a 100')
    
    elif turno == 0 and enemigo.__class__.__name__ != 'Boss':
        print(f'La empatía de {enemigo.nombre} es ***{enemigo.empatia}***')
        print('Si llegas a 50 el enemigo empatizará contigo, pero si llegas a -50 tu novia se enfadará más')                                                                                                                               
        print(f'\nEl enfado de {novia.nombre} es {novia.enfado}, evita que llegue a 100')

    elif turno != 0 and enemigo.__class__.__name__ != 'Boss':
        print(f'La empatía de {enemigo.nombre} es ***{enemigo.empatia}***')
        print(f'\nEl enfado de {novia.nombre} es {novia.enfado}, evita que llegue a 100')

def pelea_enemigo(prota, enemigo, novia):
    turno = 0
    while prota.esta_vivo() and enemigo.esta_vivo() and novia.enfado < 100:
        stun_al_prota = False
        stun_al_enemigo = False
        print(f'\nTurno {turno} ===============================================================================\n')
        informacion_batalla(prota, enemigo, novia, turno)
        print('\n_______________________________ Turno de atacar del enemigo _______________________________\n')              
        stun_al_prota = prota.defender(enemigo, stun_al_enemigo, novia)
        if novia.novia_enfadada():
            novia.enfado_maximo()
        print('\n_______________________________ Turno de atacar del prota _______________________________\n')              
        stun_al_enemigo = enemigo.defender(prota, stun_al_prota, novia)
        if novia.novia_enfadada():
            novia.enfado_maximo()
        turno += 1

    enemigo.comprobar_empatia(novia)
    
# _________________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________________

# Inicio Juego
juego_iniciado = True
print('Bienvenido al juego de discusiones más realista del mundo: WHAT HAVE I DONE?\n')
nombre_prota = input('Hola, víctima. ¿Cuál es tu nombre para referirme a ti?: ')
nombre_novia = input('Cómo se llama tu novia? (No te preocupes, no se lo diré a nadie si es inventada): ')
contador_eventos = 0
rondas = 0
motivo_del_enfado = 0

# CREACIÓN DE PERSONAJES PRINCIPALES
prota = Protagonista(nombre = nombre_prota, energia = 100, empatia = 10, dialectica = 15, nivel = 0, paciencia = 0, estado = sin_estado)

# CREACIÓN DE NPC ALIADOS
padre = Aliado('Padre', 0)
madre = Aliado('Madre', 0)
abuelo = Aliado('Abuelo', 0)
abuela = Aliado('Abuela', 0)
hermano = Aliado('Hermano', 0)
hermana = Aliado('Hermana', 0)
amigo = Aliado('Amigo', 0)
amiga = Aliado('Amiga', 0)

# VARIABLES DE JUEGO
dificultad = ''
motivo_del_enfado = ''
lista_npc_aliados = []
lista_npc_enemigos = []
lista_npc_totales = []
# _________________________________________________________________________________________________________________________

# Loop Juego
while juego_iniciado: 
    
    if prota.nivel == 0:
        
        print(f'''Encantado {nombre_prota}. Soy cupido, te pongo en situación: 
              
    Tu novia, {nombre_novia}, te ha dicho que la has cagado, pero no sabes el porqué. 
    Su respuesta a tu ignorancia es contundente: "Tú sabrás". 
    Así que decides investigar para arreglarlo. 

    Te encontrarás con enemigos que frenarán tu búsqueda y aliados que te darán 
    herramientas para mitigar la furia de tu novia. 
        
    ¿Conseguirás adivinar por qué se enfadó? 
    Y, lo más importante, 
    ¿Conseguirás arreglarlo?
            ''')
        
        dificultad = seleccion_dificultad()

        prota.subir_nivel()
        
        # CREACIÓN DE NPC
        novia, suegro, suegra, cuñado, cuñada, amigo_novia, amiga_novia = personajes_segun_dificultad(dificultad)

        lista_npc_aliados = [padre, madre, abuelo, abuela, hermano, hermana, amigo, amiga]
        lista_npc_enemigos = [suegro, suegra, cuñado, cuñada]
        # lista_npc_totales = lista_npc_aliados + lista_npc_enemigos

        # CREACIÓN DE MOTIVO DEL ENFADO
        motivo_del_enfado = random.choice(novia.lista_motivos)

        # CREACIÓN DE BOSS
        if dificultad == 'Fácil':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 2, enfado = 30, nivel = 0, paciencia = 0, estado = sin_estado)
        elif dificultad == 'Normal':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 3, enfado = 50, nivel = 0, paciencia = 1, estado = sin_estado)
        elif dificultad == 'Difícil':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 70, nivel = 1, paciencia = 2, estado = sin_estado)
        elif dificultad == 'Realista':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 8, enfado = 100, nivel = 2, paciencia = 3, estado = sin_estado)

        crear_eventos(lista_npc_totales, lista_npc_aliados, lista_npc_enemigos, dificultad)

    if contador_eventos // 7 == 0:
        crear_eventos(lista_npc_totales, lista_npc_aliados, lista_npc_enemigos, dificultad)

    if contador_eventos in [7, 14, 21]:    
        encuentro_boss(prota, novia, rondas, motivo_del_enfado, dificultad)

    if contador_eventos == 22:
        encuentro_boss(prota, novia, rondas, motivo_del_enfado, dificultad)
        print('Has terminado el juego. Has ganado.')
        sys.exit()
    else:
        print('\n')
        evento_aleatorio(lista_npc_totales, prota, novia)
        contador_eventos += 1
        








