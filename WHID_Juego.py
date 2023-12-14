from WHID_Clases import *
from WHID_Ataques import * 
from WHID_Aliados import *
import sys

# FUNCIONES

# SELECCIÓN DE DIFICULTAD
def personajes_segun_dificultad(dificultad):
    # CREACIÓN DE BOSS
    if dificultad == 1:
        dificultad_enemigos = 1

    elif dificultad == 2:
        dificultad_enemigos = 2

    elif dificultad == 3:
        dificultad_enemigos = 2

    elif dificultad == 4:
        dificultad_enemigos = 2
    
    # CREACIÓN DE NPC ENEMIGOS
    # SUEGROS
    ataque_suegro = AtaqueEnemigo(nombre = '"No vales tanto como para estar con ella"', daño = 1, nivel = 0, enfado = 0, estado = quemado_prota, empatia = 0)
    suegro = Enemigo(nombre = 'Suegro', energia = 50, empatia = 0, empatia_inicial = -30, dialectica = 5, paciencia = 1, ataque_enemigo = ataque_suegro, nivel = dificultad_enemigos, estado = sin_estado)

    ataque_suegra = AtaqueEnemigo(nombre = '"¿Aún no te ha dejado?"', daño = 0.5,  nivel = 0, enfado = 0, estado = quemado_prota, empatia = 0)
    suegra = Enemigo(nombre = 'Suegra', energia = 40, empatia = 0, empatia_inicial = -30, dialectica = 5, paciencia = 1, ataque_enemigo = ataque_suegra, nivel = dificultad_enemigos, estado = sin_estado)

    # CUÑADOS
    ataque_cuñado = AtaqueEnemigo(nombre = '"No sé de qué me hablas. Seguro que le has puesto los cuernos..."', daño = 2.5,  nivel = 0, enfado = 0, estado = paralizado_prota, empatia = 0)
    cuñado = Enemigo(nombre = 'Cuñado', energia = 60, empatia = 0, empatia_inicial = -5, dialectica = 4, paciencia = 0, ataque_enemigo = ataque_cuñado, nivel = dificultad_enemigos, estado = sin_estado)

    ataque_cuñada = AtaqueEnemigo(nombre = '"Eres un inútil."', daño = 1, nivel = 0, enfado = 0, estado = paralizado_prota, empatia = 0)
    cuñada = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0, empatia_inicial = -5, dialectica = 4, paciencia = 0, ataque_enemigo = ataque_cuñada, nivel = dificultad_enemigos, estado = sin_estado)
    
    # AMIGOS NOVIA
    ataque_amigo_novia = AtaqueEnemigo(nombre = '"Ella necesita a alguien que la quiera de verdad... Yo, por ejemplo."', daño = 5, nivel = 0, enfado = 0, estado = envenenado_prota, empatia = 0)
    amigo_novia = Enemigo(nombre = 'Amigo de la novia', energia = 40, empatia = 0, empatia_inicial = -50, dialectica = 1, paciencia = 0, ataque_enemigo = ataque_amigo_novia, nivel = dificultad_enemigos, estado = sin_estado)

    ataque_amiga_novia = AtaqueEnemigo(nombre = '"Ella puede estar con chicos mucho mejores que tú, más vale que espabiles."', daño = 0.5, nivel = 0, enfado = 0, estado = envenenado_prota, empatia = 0)
    amiga_novia = Enemigo(nombre = 'Amiga de la novia', energia = 40, empatia = 0, empatia_inicial = -5, dialectica = 5, paciencia = 0, ataque_enemigo = ataque_amiga_novia, nivel = dificultad_enemigos, estado = sin_estado)

    # ABUELOS NOVIA
    ataque_abuela_novia = AtaqueEnemigo(nombre = '"No tienes los estudios necesarios para llegar a ser alguien en la vida."', daño = 0.5, nivel = 0, enfado = 0, estado = sofocado_prota, empatia = 0)
    abuela_novia = Enemigo(nombre = 'Abuela de la novia', energia = 40, empatia = 0, empatia_inicial = 10, dialectica = 5, paciencia = 0, ataque_enemigo = ataque_abuela_novia, nivel = dificultad_enemigos, estado = sin_estado)
    
    ataque_abuelo_novia = AtaqueEnemigo(nombre = '"Chavalín, pero si tú no has hecho ni la mili, ¿Te crees que sirves de algo a la sociedad?."', daño = 0.5, nivel = 0, enfado = 0, estado = sofocado_prota, empatia = 0)
    abuelo_novia = Enemigo(nombre = 'Abuelo de la novia', energia = 40, empatia = 0, empatia_inicial = 0, dialectica = 5, paciencia = 0, ataque_enemigo = ataque_abuelo_novia, nivel = dificultad_enemigos, estado = sin_estado)
    
    # EX NOVIOS
    ataque_exnovio_reciente = AtaqueEnemigo(nombre = '"Ella es mía, no te la mereces."', daño = 2, nivel = 0, enfado = 1, estado = quemado_prota, empatia = 0)
    ex_novio_reciente = Enemigo(nombre = 'Exnovio reciente', energia = 23, empatia = 0, empatia_inicial = -40, dialectica = 5, paciencia = 0, ataque_enemigo = ataque_exnovio_reciente, nivel = dificultad_enemigos, estado = sin_estado)
    
    ataque_exnovio_antiguo = AtaqueEnemigo(nombre = '"Yo le regalé un viaje a Japón pero tú... lo único que le regalas son males de cabeza..."', daño = 2, nivel = 0, enfado = 1, estado = quemado_prota, empatia = 0)
    exnovio_antiguo = Enemigo(nombre = 'Exnovio antiguo', energia = 25, empatia = 0, empatia_inicial = -30, dialectica = 5, paciencia = 0, ataque_enemigo = ataque_exnovio_antiguo, nivel = dificultad_enemigos, estado = sin_estado)
    
    return suegro, suegra, cuñado, cuñada, amigo_novia, amiga_novia, abuela_novia, abuelo_novia, ex_novio_reciente, exnovio_antiguo

# SELECCIÓN DE DIFICULTAD
def seleccion_dificultad():
    respuesta = 0
    while respuesta not in [1, 2, 3, 4]: 
        try:
            respuesta = int(input('''Selecciona la dificultad: 
                          
    1: Nivel Fácil: Tu cagada no es tan grave y los enemigos y la novia te tienen algo de respeto
    2: Nivel Normal: Tu cagada es grave y los enemigos y la novia te tienen poco respeto
    3: Nivel Difícil: Tu cagada es muy grave y los enemigos y la novia son secos y agresivos contigo
    4: Nivel Realista: Tu cagada es tan grave que no tiene solución y tu novia está a punto de dejarte
                          
    Tu respuesta: '''))
        except ValueError:
            print('Debes introducir un número del 1 al 4')
            continue
    return respuesta

# CREADOR EVENTOS
def crear_eventos(lista_npc_totales, lista_aliados, lista_enemigos, dificultad):

    numero_enemigos = dificultad + 2
    # AÑADIR NPC ENEMIGO ALEATORIOS
    eleccion = ''
    while numero_enemigos != 0: 
        eleccion = random.choice(lista_enemigos) 
        if eleccion not in lista_npc_totales:
            lista_npc_totales.append(eleccion)
            numero_enemigos -= 1

    # AÑADIR NPC ALIADO ALEATORIOS
    cuenta_atras = [5, 4, 3, 2, 1]
    numero_aliados = cuenta_atras[dificultad]
    eleccion2 = ''
    while numero_aliados != 0: 
        eleccion2 = random.choice(lista_aliados) 
        if eleccion2 not in lista_npc_totales:
            lista_npc_totales.append(eleccion2)
            numero_aliados -= 1

    dificultad += 1
        
# EVENTOS ALEATORIOS
def evento_aleatorio(lista_npc_totales, prota, novia):
    personaje_aleatorio = random.choice(lista_npc_totales)
    print(f'Te encuentras con la siguiente persona: {personaje_aleatorio.nombre}\n')
    if personaje_aleatorio in lista_npc_enemigos: 
        print(f'Debes interactuar con {personaje_aleatorio.nombre}. ¿Preparado?\n')
        pelea_enemigo(prota, personaje_aleatorio, novia)
        print(f'\nHas ganado. Has derrotado a {personaje_aleatorio.nombre}.')
        experiencia_ganada = 25 * personaje_aleatorio.nivel
        prota.ganar_experiencia(experiencia_ganada, dificultad)
    else:
        personaje_aleatorio.eleccion_personaje(prota, novia)
    lista_npc_totales.remove(personaje_aleatorio)
    for indice, npc in enumerate(lista_npc_totales):
        print(f"- {indice}. Nombre: {npc.nombre}")

# CONTINUAR
def continuar():
    continuar = '0'
    while continuar != '':
        try:
            continuar = input('\n- - - ||| @ @ @ PARA CONTINUAR PULSA ENTER @ @ @ ||| - - -:  ')
        except ValueError:
            print('Debes pulas "ENTER')
            continue

# SISTEMA DE COMBATE
def informacion_batalla(prota, enemigo, novia, turno):
    print(f'La ENERGÍA de {prota.nombre} es ***{prota.energia}***.')
    if prota.estado != sin_estado:
        print(f'Tiene el estado "{prota.estado.nombre}" con {prota.estado.contador} turnos restantes.')
    print(f'\nLa ENERGÍA de {enemigo.nombre} es ***{enemigo.energia}***.')
    if enemigo.estado != sin_estado:
        print(f'Tiene el estado "{enemigo.estado.nombre}" con {enemigo.estado.contador} turnos restantes.')
    if turno == 0 and enemigo.__class__.__name__ == 'Boss':
        print(f'El ENFADO de tu novia {novia.nombre} es de ***{novia.enfado}***. Evita que llegue a 100')
        print(f'Con tu novia la EMPATÍA afecta directamente a su enfado. Ten cuidado.')

    elif turno != 0 and enemigo.__class__.__name__ == 'Boss':
        print(f'El ENFADO de tu novia {novia.nombre} es de ***{novia.enfado}***. Evita que llegue a 100')
    
    elif turno == 0 and enemigo.__class__.__name__ != 'Boss':
        print(f'La EMPATÍA de {enemigo.nombre} es ***{enemigo.empatia}***')
        print('Si llegas a 50 el enemigo empatizará contigo, pero si llegas a -50 tu novia se enfadará más')                                                                                                                               
        print(f'\nEl ENFADO de {novia.nombre} es {novia.enfado}, evita que llegue a 100')

    elif turno != 0 and enemigo.__class__.__name__ != 'Boss':
        print(f'La EMPATÍA de {enemigo.nombre} es ***{enemigo.empatia}***')
        print(f'\nEl ENFADO de {novia.nombre} es {novia.enfado}, evita que llegue a 100')

# PELEA 
def pelea_enemigo(prota, enemigo, novia):
    turno = 0
    while prota.esta_vivo() and enemigo.esta_vivo() and novia.enfado < 100:
        print(f'\nTurno {turno} ===============================================================================\n')
        informacion_batalla(prota, enemigo, novia, turno)
        print('\n_______________________________ ATACA EL ENEMIGO _______________________________\n')              
        prota.defender(enemigo, novia)
        continuar()
        print('\n_______________________________ ATACA EL PROTA _______________________________\n')              
        enemigo.defender(prota, novia)
        continuar()
        turno += 1

    enemigo.comprobar_empatia(novia)

# SELECCIÓN VEREDICTO
def seleccion_motivos(novia, motivo, seleccion_dificultad):
    lista_descartados = []
    if seleccion_dificultad == 1:
        dificultad = 2
    elif seleccion_dificultad == 2:
        dificultad = 4
    elif seleccion_dificultad == 3:
        dificultad = 6  
    elif seleccion_dificultad == 4:
        dificultad = 8

    print('¿Cuál crees que es la razón por la cual tu novia está enfadada?')
    print('Estas son las posibles razones: ')
    print(min(dificultad, len(novia.lista_motivos)))
    motivo = random.sample(novia.lista_motivos, min(dificultad, len(novia.lista_motivos)))
    print(motivo)
    lista_posibles_motivos = motivo
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
def encuentro_boss(prota, novia, motivo, dificultad):
    print('\nTe encuentras con el BOSS FINAL: Tu novia. \nTiene estas características: ')
    print(novia)
    print('\nEstá esperando una respuesta por tu parte:')
    pelea_enemigo(prota, novia, novia)
    print('Muy bien, la has calmado.')
    novia.subir_nivel()
    experiencia_ganada = 100 * novia.nivel
    prota.ganar_experiencia(experiencia_ganada, dificultad)
    if seleccion_motivos(novia, motivo, dificultad):
        print('Has conseguido adivinar el motivo del enfado. Has ganado.')
        print('Tu novia ahora sigue enfadada pero almenos sabes el porqué. Has... ¿ganado?')
        sys.exit()
        
# _________________________________________________________________________________________________________________________
# _________________________________________________________________________________________________________________________

# Inicio Juego
juego_iniciado = True
print('Bienvenido al juego de discusiones más realista del mundo: WHAT HAVE I DONE?\n')
nombre_prota = input('Hola, víctima. ¿Cuál es tu nombre para referirme a ti?: ')
nombre_novia = input('Cómo se llama tu novia? (No te preocupes, no se lo diré a nadie si es inventada): ')

clase_personaje = input(f'''Bien, {nombre_prota}. ¿Qué tipo de persona eres?\n
    1. Empático: Tienes más empatía con los demás, pero menos energía y dialéctica.
    2. Dialéctico: Tienes más dialéctica, pero menos empatía y energía.
    3. Energético: Tienes más energía, pero menos empatía y dialéctica.
    4. Equilibrado: Tienes las características equilibradas.\n
    Tu respuesta: ''')

# CREACIÓN DE PERSONAJES PRINCIPALES
if clase_personaje == '1':
    prota = Protagonista(nombre = nombre_prota, 
                         energia = 100, 
                         empatia = 20, 
                         dialectica = 10, 
                         nivel = 0, 
                         paciencia = 1, 
                         estado = sin_estado)
    
elif clase_personaje == '2':
    prota = Protagonista(nombre = nombre_prota, 
                         energia = 100, 
                         empatia = 10, 
                         dialectica = 20, 
                         nivel = 0, 
                         paciencia = 1, 
                         estado = sin_estado)
    
elif clase_personaje == '3':
    prota = Protagonista(nombre = nombre_prota, 
                         energia = 200, 
                         empatia = 10, 
                         dialectica = 10, 
                         nivel = 0, 
                         paciencia = 5, 
                         estado = sin_estado)
    
elif clase_personaje == '4':
    prota = Protagonista(nombre = nombre_prota, 
                         energia = 150, 
                         empatia = 15, 
                         dialectica = 15, 
                         nivel = 0, 
                         paciencia = 2, 
                         estado = sin_estado)

# CREACIÓN DE NPC ALIADOS
padre = Aliado('Padre', 0)
madre = Aliado('Madre', 0)
abuelo = Aliado('Abuelo', 0)
abuela = Aliado('Abuela', 0)
hermano = Aliado('Hermano', 0)
hermana = Aliado('Hermana', 0)
amigo = Aliado('Amigo', 0)
amiga = Aliado('Amiga', 0)
compañero_clase = Aliado('Compañero de clase', 0)
compañera_clase = Aliado('Compañera de clase', 0)
perro = Aliado('Perro', 0)
gato = Aliado('Gato', 0)

# VARIABLES DE JUEGO
dificultad = 0
motivo_del_enfado = ''
contador_eventos = 0
lista_npc_aliados = []
lista_npc_enemigos = []
lista_npc_totales = []
# _________________________________________________________________________________________________________________________

# Loop Juego
while juego_iniciado: 
    if prota.nivel == 0:
        
        print(f'''\nEncantado {nombre_prota}. Soy cupido, te pongo en situación: \n
    Tu novia, {nombre_novia}, te ha dicho que la has cagado, pero no sabes el porqué. 
    Su respuesta a tu ignorancia es contundente: "Tú sabrás". 
    Así que decides investigar para arreglarlo. \n
    Te encontrarás con enemigos que frenarán tu búsqueda y aliados que te darán 
    herramientas para mitigar la furia de tu novia. \n
    ¿Conseguirás adivinar por qué se enfadó? 
    Y, lo más importante, \n
    ¿Conseguirás arreglarlo?\n
    Buena suerte, la vas a necesitar.\n''')
        
        dificultad = seleccion_dificultad()

        # CREACIÓN DE BOSS
        if dificultad == 1:
            novia = Boss(nombre = nombre_novia, energia = 100, empatia = 0, dialectica = 2, enfado = 20, nivel = 0, paciencia = 0, estado = sin_estado)
        elif dificultad == 2:
            novia = Boss(nombre = nombre_novia, energia = 125, empatia = 0, dialectica = 3, enfado = 40, nivel = 0, paciencia = 1, estado = sin_estado)
        elif dificultad == 3:
            novia = Boss(nombre = nombre_novia, energia = 150, empatia = 0, dialectica = 5, enfado = 60, nivel = 1, paciencia = 2, estado = sin_estado)
        elif dificultad == 4:
            novia = Boss(nombre = nombre_novia, energia = 250, empatia = 0, dialectica = 8, enfado = 80, nivel = 2, paciencia = 3, estado = sin_estado)

        # CREACIÓN DE MOTIVO DEL ENFADO
        motivo_del_enfado = random.choice(novia.lista_motivos)

        prota.ganar_experiencia(0, dificultad)
        
        # CREACIÓN DE NPC
        suegro, suegra, cuñado, cuñada, amigo_novia, amiga_novia, abuela_novia, abuelo_novia, ex_novio_reciente, exnovio_antiguo = personajes_segun_dificultad(dificultad)

        lista_npc_aliados = [padre, madre, abuelo, abuela, hermano, hermana, amigo, amiga, compañero_clase, compañera_clase, perro, gato]
        lista_npc_enemigos = [suegro, suegra, cuñado, cuñada, amigo_novia, amiga_novia, abuela_novia, abuelo_novia, ex_novio_reciente, exnovio_antiguo]

        # CREACIÓN DE EVENTOS
        crear_eventos(lista_npc_totales, lista_npc_aliados, lista_npc_enemigos, dificultad)
        print(f'Esta es la lista de npc totales: \n')
        for indice, npc in enumerate(lista_npc_totales):
            print(f"- {indice}. Nombre: {npc.nombre}")

    if contador_eventos in [7, 14, 21]:    
        encuentro_boss(prota, novia, motivo_del_enfado, dificultad)
        print('No has conseguido adivinar el motivo del enfado. Debes seguir investigando.')
        print(f'Has hecho {contador_eventos} eventos. Te quedan {28 - contador_eventos} eventos para adivinarlo.')
        print(f'Esta es la lista de npc totales tras el boss: ')
        for indice, npc in enumerate(lista_npc_totales):
            print(f"Índice: {indice}, Nombre: {npc.nombre}")
        crear_eventos(lista_npc_totales, lista_npc_aliados, lista_npc_enemigos, dificultad)
        for indice, npc in enumerate(lista_npc_totales):
            print(f"Índice: {indice}, Nombre: {npc.nombre}")
        print(f'Se han añadido más personajes al juego.')
        contador_eventos += 1

    if contador_eventos == 28:
        encuentro_boss(prota, novia, motivo_del_enfado, dificultad)

    else:
        print(f'\nHas hecho {contador_eventos} eventos. Te quedan {28 - contador_eventos} eventos.')
        evento_aleatorio(lista_npc_totales, prota, novia)
        contador_eventos += 1
        








