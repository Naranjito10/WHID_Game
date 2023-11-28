from WHID_Clases import *
from random import randint
import sys

novia = Boss('Ángela', 40, 60, 5, 50)
padre = Personaje('Juan', 30, 50, 10)
kevin = Protagonista('Kevin', 100, 50, 10, 0)

suegro = Personaje('Suegro', 50, 20, 15)
suegra = Personaje('Suegra', 50, 40, 20)
cuñado = Personaje('Cuñado', 50, 50, 20)
cuñada = Personaje('Cuñada', 50, 30, 10)

padre = True
madre = True

juego_iniciado = True
lista_personajes = [padre, madre, suegro, suegra, cuñado, cuñada]

def pelea_enemigo(prota, enemigo):
    while prota.energia > 0 and enemigo.energia > 0:
        daño = prota.eleccion_ataque()
        novia.defender(prota.ataque(daño))

nombre = input('¿Cuál es tu nombre?: ')
prota = Protagonista(nombre, 100, 50, 10, 0)


while juego_iniciado: 
    if prota.nivel == 0:
        print(f'''Hola {nombre}. Tu novia te ha dicho que la has cagado, pero no sabes el porqué. 
            Su respuesta a tu ignorancia: un contundente "Tú sabrás". 
            Así que decides investigar para intentar arreglarlo. 
            Te encontrarás con enemigos que frenarán tu búsqueda y aliados que te darán herramientas 
            para mitigar la furia de tu novia. 
            ¿Conseguirás adivinar por qué se enfadó? 
            Y, lo más importante, ¿Conseguirás arreglarlo?''')
        prota.subir_nivel()
    else:     
        print('\nTe encuentras con tu novia. Tiene estas características: ')
        print(novia)
        print('\nEstá esperando una respuesta por tu parte:')
        pelea_enemigo(prota, novia)
        print('Muy bien, la has calmado.')
        prota.subir_nivel()




        # personaje_aleatorio = randint(lista_personajes)
        # print(f'Te encuentras con la siguiente personas: {personaje_aleatorio}')
        # if personaje_aleatorio == suegro: 
        #     pelea_enemigo(prota, suegro)

        # elif personaje_aleatorio == suegra:








