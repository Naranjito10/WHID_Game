from random import randint
import random
from WHID_Ataques import *

class Personaje: 

    def __init__(self, nombre, energia, empatía, labia):
        self.nombre = nombre
        self.energia = energia
        self.empatía = empatía
        self.labia = labia
            
    def __str__(self):
        return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatía}, Labia: {self.labia}"
    
    def ataque(self, ataque_propio): 
        resultado = self.labia * ataque_propio
        print(f"{self.nombre} ataca con una fuerza total de {resultado}")
        return resultado
    
    def defender(self, ataque_contrincante): 
        self.energia = self.energia - ataque_contrincante
        print(f"{self.nombre} se defiende contra un ataque de {ataque_contrincante} y le baja la paciencia a {self.energia}")
        
class Protagonista(Personaje):

    lista_arg_razonable = [
                    {'id': 1, 
                  'arg_1': 'Tienes razón', 
                  'Fuerza': 5, 
                  'Estado': 'Quemado'}, 
                  {'id': 2, 
                  'arg_1': 'Lo siento', 
                  'Fuerza': 10}
                  ]
    
    lista_acc_amistosa = [
                    {'id': 1, 
                  'arg_1': 'Amo al cine', 
                  'Fuerza': 5}, 
                  {'id': 2, 
                  'arg_1': 'Amo al teatro', 
                  'Fuerza': 10}
                  ]
    
    lista_ata_toxico = [{'id': 1, 
                  'arg_1': 'Eres tú', 
                  'Fuerza': 5}, 
                  {'id': 2, 
                  'arg_1': 'Soy así', 
                  'Fuerza': 10}]
    
    lista_arg_cutre = [{'id': 1, 
                  'arg_1': 'El qué?', 
                  'Fuerza': 5}, 
                  {'id': 2, 
                  'arg_1': 'Yo?', 
                  'Fuerza': 10}]

    def __init__(self, nombre, energia, empatía, labia, nivel):
        super().__init__(nombre, energia, empatía, labia)

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
        return ataque_final, daño
        
    
class Boss(Personaje):

    ataques = {'Ataque Poderoso': 10, 
               'Ataque Débil': 5}
    
    def __init__(self, nombre, energia, empatía, labia, enfado):
        super().__init__(nombre, energia, empatía, labia)
            
        self.enfado = enfado

    def __str__(self):
        return f"Nombre: {self.nombre}, Energia: {self.energia}, Empatía: {self.empatía}, Labia: {self.labia}, Enfado: {self.enfado}"

    
