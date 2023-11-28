import random

class Estados: 
    def __init__(self, nombre, probabilidad_dar, daño, probabilidad_afectar):
        self.nombre = nombre
        self.probabilidad_dar = probabilidad_dar
        self.daño = daño
        self.probabilidad_afectar = probabilidad_afectar

class Ataque: 

    # lista_ataques_totales = []

    def __init__(self, nombre, daño, empatia, categoria):
        self.nombre = nombre
        self.daño = daño
        self.empatia = empatia
        self.categoria = categoria
        # self.lista_ataques_totales.append(Ataque)
        

    def atacar_1(self):
        return f"{self.nombre} hace {self.daño} de daño."

    def agrega_estado(self, estado):
        pass

    def get_lista_ataques_totales(self):
        return self.lista_ataques_totales

# CLASE DEL PROTA
class AtaqueProta(Ataque):

    lista_ataques_totales = []

    arg_razonable = []
    acc_amistosa = []
    arg_cutre = []
    arg_toxico = []

    lista_ataques_prota = [arg_razonable, acc_amistosa, arg_cutre, arg_toxico] 

    def __init__(self, nombre, daño, empatia, categoria, nivel):
        super().__init__(nombre, daño, empatia, categoria)
        self.nivel = nivel
        AtaqueProta.añadir_iniciales(AtaqueProta)
    
    @classmethod
    def añadir_iniciales(cls, AtaqueProta):
        cls.lista_ataques_totales.append(AtaqueProta)
        if cls.nivel == 0: 
            if cls.categoria == 'arg_cutre':
                cls.arg_cutre.append(AtaqueProta)
            elif cls.categoria == 'arg_razonable':
                cls.arg_razonable.append(AtaqueProta)
            elif cls.categoria == 'arg_toxico':
                cls.arg_toxico.append(AtaqueProta)
            elif cls.categoria == 'acc_amistosa':
                cls.acc_amistosa.append(AtaqueProta)
            else:
                print('Hay un error')

    @classmethod
    def subir_nivel(cls, nivel): 
        print(cls.lista_ataques_totales)
        for i in cls.lista_ataques_totales:
            if i.nivel == nivel:
                if i.categoria == 'arg_cutre':
                    self.arg_cutre.append(i)
                elif i.categoria == 'arg_razonable':
                    self.arg_razonable.append(i)
                elif i.categoria == 'arg_toxico':
                    self.arg_toxico.append(i)
                elif i.categoria == 'acc_amistosa':
                    self.acc_amistosa.append(i)
                else:
                    print('Hay un error')
            else:
                continue

    def __str__(self):
        return f"Nombre: {self.nombre}, Daño: {self.daño}, Empatía: {self.empatia}, Categoria: {self.categoria}, Nivel: {self.nivel}"    
        
    def subir_nivel111(self):
        for i in self.lista_ataques_totales:
            if i.nivel == 0:
                if self.categoria == 'arg_cutre':
                    self.arg_cutre.append(AtaqueProta)
                elif self.categoria == 'arg_razonable':
                    self.arg_razonable.append(AtaqueProta)
                elif self.categoria == 'arg_toxico':
                    self.arg_toxico.append(AtaqueProta)
                elif self.categoria == 'acc_amistosa':
                    self.acc_amistosa.append(AtaqueProta)
                else:
                    print('Hay un error')
                self.lista_ataques_prota.append()
        
    def habilidades_subir_nivel(self):
        pass

    def habilidades_inicio(self):
        pass

ataque1 = AtaqueProta('"Tienes Razón"', 0.5, 10, 'arg_razonable', 0)
ataque2 = AtaqueProta('"No es verdad"', 1, -5, 'arg_cutre', 0)
ataque3 = AtaqueProta('"tóxico man"', 2, -10, 'arg_toxico', 0)
ataque4 = AtaqueProta('"vamos al cine"', 1.5, 5, 'acc_amistosa', 1)

# print(AtaqueProta.lista_ataques_prota)
ataque1.subir_nivel(1)
print(ataque1)
print(AtaqueProta.lista_ataques_prota)



class AtaqueBoss(Ataque):

    lista_ataques_boss = []

    def __init__(self, nombre, daño, empatia, categoria):
        super().__init__(nombre, daño, empatia, categoria)
        
    def habilidades_inicio(self):
        pass

class AtaqueProta(Ataque):

    lista_ataques_enemigo = []

    def __init__(self, nombre, daño, empatia, categoria):
        super().__init__(nombre, daño, empatia, categoria)
        
    def habilidades_inicio(self):
        pass
        
        
    # Probar de hacer los ataques con clase



# print(lista_ataques[0].atacar_1())
# print(ataque1.get_lista_ataques_totales())


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

    

