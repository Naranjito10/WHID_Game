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

# CREACIÓN DE PERSONAJES PRINCIPALES
prota = Protagonista(nombre = nombre_prota, energia = 100, empatia = 10, dialectica = 10, nivel = 0)
novia = Boss(nombre = nombre_novia, energia = 40, empatia = 60, dialectica = 5, enfado = 50, nivel = 0)

# CREACIÓN DE NPC ALIADOS
padre = Enemigo('Padre', 40, 60, 5, 50, 0)
madre = Enemigo('Madre', 40, 60, 5, 50, 0)

# CREACIÓN DE NPC ENEMIGOS
ataque_suegro = AtaqueEnemigo(nombre = '"No vales tanto como para estar con ella"', daño = 0.5, estado = quemado)
suegro = Enemigo(nombre = 'Suegro', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegro)

ataque_suegra = AtaqueEnemigo(nombre = '"¿Aún no te ha dejado?"', daño = 0.5, estado = quemado)
suegra = Enemigo(nombre = 'Suegra', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_suegra)

ataque_cuñado = AtaqueEnemigo(nombre = '"No sé de qué me hablas. Seguro que le has puesto los cuernos..."', daño = 5, estado = paralizado)
cuñado = Enemigo(nombre = 'Cuñado', energia = 40, empatia = 0, dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñado)

ataque_cuñada = AtaqueEnemigo(nombre = '"Eres un inútil."', daño = 0.5, estado = paralizado)
cuñada = Enemigo(nombre = 'Cuñada', energia = 40, empatia = 0,dialectica = 5, enfado = 50, ataque_enemigo = ataque_cuñada)

# CREACIÓN DE NPC
lista_npc_aliados = [padre, madre]
lista_npc_enemigos = [suegro, suegra, cuñado, cuñada]
lista_npc_totales = lista_npc_aliados + lista_npc_enemigos

# SELECCIÓN VEREDICTO
def seleccion_veredicto():
    False

def encuentro_personaje(prota, personaje_aleatorio):
    pass

# ENCUENTROS CON BOSS
def encuentro_boss(prota, novia, rondas):
    print('\nTe encuentras con el BOSS FINAL: Tu novia. \nTiene estas características: ')
    print(novia)
    print('\nEstá esperando una respuesta por tu parte:')
    pelea_enemigo(prota, novia)
    print('Muy bien, la has calmado.')
    novia.subir_nivel()
    prota.subir_nivel()
    if seleccion_veredicto():
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
    else:
        print(f'Te encuentras con la siguiente persona: {personaje_aleatorio.nombre}')
        print(f'{personaje_aleatorio} te ofrece dos herramientaa para mitigar el enfado de tu novia. ¿Cuál escoges?')
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
    
    if contador_eventos == 16:
        print('Has terminado el juego. Has ganado.')
        sys.exit()

    if contador_eventos == 0:    
        encuentro_boss(prota, novia, rondas)
    else:
        print('\n')
        evento_aleatorio(lista_npc_totales, prota.nivel)
        prota.subir_nivel()
        contador_eventos += 1
        








