import random

class Estados: 
    def __init__(self, nombre, probabilidad_dar, daño, probabilidad_afectar):
        self.nombre = nombre
        self.probabilidad_dar = probabilidad_dar
        self.daño = daño
        self.probabilidad_afectar = probabilidad_afectar

estados = [{'id': 1, 
                  'arg_1': 'Tienes razón', 
                  'Fuerza': 5,
                  'Categoria': 'arg_razonables'}]

arg_razonables = [{'id': 1, 
                  'arg_1': 'Tienes razón', 
                  'Fuerza': 5,
                  'Categoria': 'arg_razonables'}, 
                  {'id': 2, 
                  'arg_1': 'Lo siento', 
                  'Fuerza': 10,
                  'Categoria': 'arg_razonables'},
                  {'id': 3, 
                  'arg_1': 'Eres la mejor', 
                  'Fuerza': 5,
                  'Categoria': 'arg_razonables'}, 
                  {'id': 4, 
                  'arg_1': 'Dime porfa que pasó', 
                  'Fuerza': 10,
                  'Categoria': 'arg_razonables'}]

acc_amistosa = [{'id': 1, 
                  'arg_1': 'Amo al cine', 
                  'Fuerza': 5,
                  'Categoria': 'acc_amistosa'}, 
                  {'id': 2, 
                  'arg_1': 'Amo al teatro', 
                  'Fuerza': 10,
                  'Categoria': 'acc_amistosa'},
                  {'id': 3, 
                  'arg_1': 'Compramos comida?', 
                  'Fuerza': 5,
                  'Categoria': 'acc_amistosa'}, 
                  {'id': 4, 
                  'arg_1': 'Quieres chuches?', 
                  'Fuerza': 10,
                  'Categoria': 'acc_amistosa'}]

ata_toxico = [{'id': 1, 
                  'arg_1': 'Eres tú', 
                  'Fuerza': 5,
                  'Categoria': 'ata_toxico',
                  'Estado': 'Quemado',
                  'Probabilidad_efecto': 0.30}, 
                  {'id': 2, 
                  'arg_1': 'Soy así', 
                  'Fuerza': 10,
                  'Categoria': 'ata_toxico',
                  'Estado': 'Congelado',
                  'Probabilidad_efecto': 0.30},
                  {'id': 3, 
                  'arg_1': 'Tu culpa', 
                  'Fuerza': 5,
                  'Categoria': 'ata_toxico',
                  'Estado': 'Paralizado',
                  'Probabilidad_efecto': 0.30}, 
                  {'id': 4, 
                  'arg_1': 'Mi padre me hizo asi', 
                  'Fuerza': 10,
                  'Categoria': 'ata_toxico',
                  'Estado': 'Congelado',
                  'Probabilidad_efecto': 0.30}]

arg_cutre = [{'id': 1, 
                  'arg_1': 'El qué?', 
                  'Fuerza': 5,
                  'Categoria': 'arg_cutre'}, 
                  {'id': 2, 
                  'arg_1': 'Yo?', 
                  'Fuerza': 10,
                  'Categoria': 'arg_cutre'},
                  {'id': 3, 
                  'arg_1': 'Nosé', 
                  'Fuerza': 5,
                  'Categoria': 'arg_cutre'}, 
                  {'id': 4, 
                  'arg_1': 'De qué hablas?', 
                  'Fuerza': 10,
                  'Categoria': 'arg_cutre'}]

def añadir_habilidad_nivel(nivel):
    lista_habilidades_nivel = [[1, 2],
                               [3, 4]]
    nivel_escogido = lista_habilidades_nivel[nivel - 1]
    ataque_final1 = 0
    ataque_final2 = 0
    while ataque_final1 == ataque_final2:
        numero_aleatorio1 = random.choice(nivel_escogido)
        numero_aleatorio2 = random.choice(nivel_escogido)
        lista_categorias = [arg_cutre, arg_razonables, acc_amistosa, ata_toxico]
        categoria_seleccionada1 = lista_categorias[random.choice(range(0, len(lista_categorias) - 1))]
        categoria_seleccionada2 = lista_categorias[random.choice(range(0, len(lista_categorias) - 1))]
        dict_seleccionado1 = list(e for e in categoria_seleccionada1 if e['id']  == numero_aleatorio1)[0]
        dict_seleccionado2 = list(e for e in categoria_seleccionada2 if e['id']  == numero_aleatorio2)[0]
        ataque_final1 = dict_seleccionado1.get('arg_1')
        ataque_final2 = dict_seleccionado2.get('arg_1')
        categoria1 = dict_seleccionado1.get('Categoria')
        categoria2 = dict_seleccionado2.get('Categoria')
        # añadir el pop de la lista para que no se vuelva a escoger
    
    print(f'''Habilidades para escoger: 
            - 1. {ataque_final1} 
            - 2. {ataque_final2}''')
    opcion_escogida = input('¿Qué habilidad escoges?: ')
    if opcion_escogida == '1': 
        return categoria1, ataque_final1, dict_seleccionado1
    elif opcion_escogida == '2': 
        return categoria2, ataque_final2, dict_seleccionado2

    

