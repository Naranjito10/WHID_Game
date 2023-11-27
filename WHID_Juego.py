from WHID_Clases import *
import sys

novia = Boss('Ángela', 40, 60, 5, 50)
padre = Personaje('Juan', 30, 50, 10)
kevin = Protagonista('Kevin', 100, 50, 10, 0)



kevin.subir_nivel()
print('')
print('Te encuentras con tu novia.')
print('Tiene estas características: ')
print(novia)
print('')
print('Está muy enfadada pero no sabes porqué. Está esperando una respuesta por tu parte:')
print('')
ataque, daño = kevin.eleccion_ataque()
novia.defender(kevin.ataque(daño))
print('Muy bien, la has calmado.')
kevin.subir_nivel()