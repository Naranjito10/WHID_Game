from WHID_Clases import *
from WHID_Ataques import *
from random import randint
import sys


# Inicio Juego
juego_iniciado = True
print('Bienvenido al juego de discusiones más realista del mundo: WHAT HAVE I DONE?\n')
nombre_prota = input('Hola, víctima. ¿Cuál es tu nombre para referirme a ti?: ')
nombre_novia = input('Cómo se llama tu novia? (No te preocupes, no se lo diré a nadie si es inventada): ')
contador_eventos = 0
rondas = 0
motivo_del_enfado = 0

# CREACIÓN DE PERSONAJES PRINCIPALES
prota = Protagonista(nombre = nombre_prota, energia = 100, empatia = 10, dialectica = 10, nivel = 0)

# CREACIÓN DE NPC ALIADOS
padre = Enemigo('Padre', 40, 60, 5, 50, 0)
madre = Enemigo('Madre', 40, 60, 5, 50, 0)



# CREACIÓN DE NPC
lista_npc_aliados = [padre, madre]
lista_npc_enemigos = [suegro, suegra, cuñado, cuñada]
lista_npc_totales = lista_npc_aliados + lista_npc_enemigos


# SELECCIÓN DE DIFICULTAD
def personajes_segun_dificultad(dificultad):
    # CREACIÓN DE BOSS
    if dificultad == 'Fácil':
        novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 0)
    elif dificultad == 'Normal':
        novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 0)
    elif dificultad == 'Difícil':
        novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 1)
    elif dificultad == 'Realista':
        novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 2)

    # CREACIÓN DE NPC ENEMIGOS
    ataque_suegro = AtaqueEnemigo(nombre = '"No vales tanto como para estar con ella"', daño = 0.5, nivel = 0, enfado = 0, estado = quemado)
    ataque_suegra = AtaqueEnemigo(nombre = '"¿Aún no te ha dejado?"', daño = 0.5,  nivel = 0, enfado = 0, estado = quemado)
    ataque_cuñado = AtaqueEnemigo(nombre = '"No sé de qué me hablas. Seguro que le has puesto los cuernos..."', daño = 5,  nivel = 0, enfado = 0, estado = paralizado)
    ataque_cuñada = AtaqueEnemigo(nombre = '"Eres un inútil."', daño = 0.5, nivel = 0, enfado = 0, estado = paralizado)

    if dificultad == 'Fácil':
        suegro = Enemigo(nombre = 'Suegro', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegro)
        suegra = Enemigo(nombre = 'Suegra', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegra)
        cuñado = Enemigo(nombre = 'Cuñado', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñado)
        cuñada = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñada)

    elif dificultad == 'Normal':
        suegro = Enemigo(nombre = 'Suegro', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegro)
        suegra = Enemigo(nombre = 'Suegra', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegra)
        cuñado = Enemigo(nombre = 'Cuñado', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñado)
        cuñada = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñada)

    elif dificultad == 'Difícil':
        suegro = Enemigo(nombre = 'Suegro', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegro)
        suegra = Enemigo(nombre = 'Suegra', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegra)
        cuñado = Enemigo(nombre = 'Cuñado', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñado)
        cuñada = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñada)

    elif dificultad == 'Realista':  
        suegro = Enemigo(nombre = 'Suegro', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegro)
        suegra = Enemigo(nombre = 'Suegra', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegra)
        cuñado = Enemigo(nombre = 'Cuñado', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñado)
        cuñada = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñada)

    return novia, suegro, suegra, cuñado, cuñada

def seleccion_dificultad():
    print('Selecciona la dificultad: ')
    print('1: Fácil')
    print('2: Normal')
    print('3: Difícil')
    print('4: Realista')
    respuesta = int(input('Selecciona la dificultad: '))
    if respuesta == 1:
        return 'Fácil'
    elif respuesta == 2:
        return 'Normal'
    elif respuesta == 3:
        return 'Difícil'
    elif respuesta == 4:
        return 'Realista'
    else:
        print('No has seleccionado una dificultad válida. Vuelve a intentarlo.')
        seleccion_dificultad()

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
    pelea_enemigo(prota, novia)
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

# EVENTOS ALEATORIOS
def evento_aleatorio(lista, nivel):
    personaje_aleatorio = random.choice(lista)
    if personaje_aleatorio in lista_npc_enemigos: 
        print(f'Te encuentras con la siguiente persona: {personaje_aleatorio}')
        print(f'Debes interactuar con {personaje_aleatorio}. ¿Qué haces?')
        pelea_enemigo(prota, personaje_aleatorio)
        prota.subir_nivel()
    else:
        print(f'Te encuentras con la siguiente persona: {personaje_aleatorio.nombre}')
        print(f'{personaje_aleatorio} te ofrece dos herramientaa para mitigar el enfado de tu novia. ¿Cuál escoges?')
        Aliado.eleccion_personaje()
        seleccionar_nuevo_ataque(nivel)

# SISTEMA DE COMBATE
def pelea_enemigo(prota, enemigo):
    while prota.esta_vivo() and enemigo.esta_vivo():
        print(f'La energía de {prota.nombre} es {prota.energia}')
        print(f'La energía de {enemigo.nombre} es {enemigo.energia}')
        ataque_escogido_prota = prota.eleccion_ataque()
        ataque_escogido_enemigo = enemigo.eleccion_ataque()
        prota.trigger_estado()
        prota.defender(ataque_escogido_enemigo, enemigo.dialectica)
        enemigo.trigger_estado()
        enemigo.defender(ataque_escogido_prota, prota.dialectica)
       

        print('\n__________________________________________________________\n')
    

# _________________________________________________________________________________________________________________________

# Loop Juego
while juego_iniciado: 
    if prota.nivel == 0:
        print(f'''Encantado {nombre_prota}. Soy cupido, te pongo en situación: 
              
            Tu novia, {nombre_novia}, te ha dicho que la has cagado, pero no sabes el porqué. 
            Su respuesta a tu ignorancia es contundente: "Tú sabrás". 
            Así que decides investigar para arreglarlo. 

            Te encontrarás con enemigos que frenarán tu búsqueda y aliados que te darán herramientas 
            para mitigar la furia de tu novia. 
              
            ¿Conseguirás adivinar por qué se enfadó? 
            Y, lo más importante, 
            ¿Conseguirás arreglarlo?''')

        prota.subir_nivel()
        dificultad = seleccion_dificultad()
        motivo_del_enfado = random.choice(novia.lista_motivos)
        personajes_segun_dificultad(dificultad)
        if dificultad == 'Fácil':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 0)
        elif dificultad == 'Normal':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 0)
        elif dificultad == 'Difícil':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 1)
        elif dificultad == 'Realista':
            novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 2)
    
    if contador_eventos == 16:
        encuentro_boss(prota, novia, rondas, dificultad)
        print('Has terminado el juego. Has ganado.')
        sys.exit()

    if contador_eventos == 8:    
        encuentro_boss(prota, novia, rondas, motivo_del_enfado, dificultad)
    else:
        print('\n')
        evento_aleatorio(lista_npc_totales, prota.nivel, dificultad)
        contador_eventos += 1
        








