from WHID_Clases import *
from random import randint

suegro = Personaje('Suegro', 50, 20, 15)
suegra = Personaje('Suegra', 50, 40, 20)
cuñado = Personaje('Cuñado', 50, 50, 20)
cuñada = Personaje('Cuñada', 50, 30, 10)

padre = True
madre = True

juego_iniciado = True
lista_personajes = [padre, madre, suegro, suegra, cuñado, cuñada]

def pelea_enemigo(prota, enemigo):
    while prota.energia > 0 or enemigo.energia < 0:
        enemigo.atacar


while juego_iniciado: 
    print('''Tu novia te ha dicho que la has cagado, pero no sabes el porqué. 
          Ella te responde, tú sabrás. Así que decides investigar para intentar arreglarlo. 
          Te encontrarás con enemigos que frenarán tu búsqueda y aliados que te darán herramientas 
          para mitigar la furia de tu novia. 
          ¿Conseguirás adivinar por qué se enfadó? 
          Y, lo más importante, ¿Conseguirás arreglarlo?''')
    
    nombre = input('¿Cuál es tu nombre?')
    prota = Personaje(nombre, 50, 50, 1, 10)
    personaje_aleatorio = randint(lista_personajes)
    print(f'Te encuentras con la siguiente personas: {personaje_aleatorio}')
    if personaje_aleatorio == suegro: 
        pelea_enemigo(prota, suegro)

    elif personaje_aleatorio == suegra:


resultado_ataque = primo.atacar(10)
resultado_defensa = padre.defender(resultado_ataque)
print(resultado_defensa)