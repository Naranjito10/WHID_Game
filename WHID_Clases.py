from random import randint
import random
from WHID_Ataques import *

class Personaje: 

    def __init__(self, nombre, energia, empatia, dialectica):
        self.nombre = nombre
        self.energia = energia
        self.empatia = empatia
        self.dialectica = dialectica
            
    def __str__(self):
        return f"Nombre: {self.nombre}, Energía: {self.energia}, Empatía: {self.empatia}, Dialéctica: {self.dialectica}"

    def subir_nivel(self, energia, empatia, dialectica):
        self.energia = self.energia + energia
        self.empatia = self.empatia + empatia
        self.dialectica = self.dialectica + dialectica

    def esta_vivo(self):
        return self.energia > 0
    
    def morir(self):
        self.energia = 0
        print(self.nombre, "se ha quedado sin energia para seguir discutiendo")

    def atacar(self, ataque_propio): 
        resultado = self.dialectica * ataque_propio.daño()
        print(f"{self.nombre} ataca con una fuerza total de {resultado}")
        return resultado
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
    
    def defender(self, ataque_contrincante): 
        self.energia = self.energia - ataque_contrincante
        print(f"{self.nombre} se defiende contra un ataque de {ataque_contrincante} y le baja la energia a {self.energia}")
        if self.energia < 0:
            print('Has acabado con la energia del enemigo')
        elif estado : 
            # Aplicar estado
            print()
        
        
class Protagonista(Personaje):

    lista_arg_razonable = [
                    {'id': 1, 
                  'arg_1': 'Tienes razón', 
                  'Fuerza': 5, 
                  'Estado': 'Quemado'
                  'Nivel 0'}, 
                  {'id': 2, 
                  'arg_1': 'Lo siento', 
                  'Fuerza': 10, 
                  'Estado': 'Quemado'
                  'Nivel 0'}
                  ]
    
    lista_acc_amistosa = [
                    {'id': 1, 
                  'arg_1': 'Amo al cine', 
                  'Fuerza': 5, 
                  'Estado': 'Quemado'
                  'Nivel 0'}, 
                  {'id': 2, 
                  'arg_1': 'Amo al teatro', 
                  'Fuerza': 10, 
                  'Estado': 'Quemado'
                  'Nivel 0'}
                  ]
    
    lista_ata_toxico = [{'id': 1, 
                  'arg_1': 'Eres tú', 
                  'Fuerza': 5, 
                  'Estado': 'Quemado'
                  'Nivel 0'}, 
                  {'id': 2, 
                  'arg_1': 'Soy así', 
                  'Fuerza': 10, 
                  'Estado': 'Quemado'
                  'Nivel 0'}]
    
    lista_arg_cutre = [{'id': 1, 
                  'arg_1': 'El qué?', 
                  'Fuerza': 5, 
                  'Estado': 'Quemado'
                  'Nivel 0'}, 
                  {'id': 2, 
                  'arg_1': 'Yo?', 
                  'Fuerza': 10, 
                  'Estado': 'Quemado'
                  'Nivel 0'}]

    def __init__(self, nombre, energia, empatía, dialectica, nivel):
        super().__init__(nombre, energia, empatía, dialectica)

        # Añadimos un atributo nuevo
        self.nivel = nivel
    
    def subir_nivel(self):
        self.nivel += 1
        if self.nivel == 1:
            print(f'Ahora eres nivel {self.nivel}, escoge entre estas dos habilidades para añadir a tu kit inicial: ')
        else: 
            print(f'Acabas de subir al nivel {self.nivel}, escoge entre estas dos habilidades para añadir a tu kit: ')
        categoria, habilidad_escogida, dict_escogido = añadir_habilidad_nivel(self.nivel)
        if categoria == 'arg_razonables':
            self.lista_arg_razonable.append(dict_escogido)
        elif categoria == 'acc_amistosa':
            self.lista_acc_amistosa.append(dict_escogido)
        elif categoria == 'ata_toxico':
            self.lista_ata_toxico.append(dict_escogido)
        elif categoria == 'arg_cutre':
            self.lista_arg_cutre.append(dict_escogido)

        print(f'Muy bien, has añadido la habilidad {habilidad_escogida} en la categoría {categoria}')

    
    
    def eleccion_ataque(self):
        print('''Acciones disponibles: 
                - 1. Argumento razonable
                - 2. Acción amistosa 
                - 3. Ataque toxico 
                - 4. Argumento cutre
              ''')
        ataque_elegido = input('Qué deseas realizar?: ')
        if ataque_elegido == '1':
            categoria_elegida = self.lista_arg_razonable
        elif ataque_elegido == '2':
            categoria_elegida = self.lista_acc_amistosa
        elif ataque_elegido == '3':
            categoria_elegida = self.lista_ata_toxico        
        elif ataque_elegido == '4':
            categoria_elegida = self.lista_arg_cutre
        
        numero_aleatorio = random.choice(range(0, len(categoria_elegida) - 1))
        dict_ataque = categoria_elegida[numero_aleatorio]
        ataque_final = dict_ataque.get('arg_1')
        daño = dict_ataque.get('Fuerza')
        print(f"{self.nombre} ataca con '{ataque_final}' con una fuerza de {daño}")
        return daño
        
    
class Boss(Personaje):

    ataques = {'Ataque Poderoso': 10, 
               'Ataque Débil': 5}
    
    def __init__(self, nombre, energia, empatia, dialectica, enfado):
        super().__init__(nombre, energia, empatia, dialectica)
            
        self.enfado = enfado

    def __str__(self):
        return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatia}, Dialectica: {self.dialectica}, Enfado: {self.enfado}"

    
