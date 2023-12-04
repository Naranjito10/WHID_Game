import random

class Estado: 
    def __init__(self, nombre: str, probabilidad_afectar: int, probabilidad_trigger: int, contador: int, daño: int = None, efecto: str = None):
        self.nombre = nombre
        self.probabilidad_afectar = probabilidad_afectar
        self.probabilidad_trigger = probabilidad_trigger
        self.contador = contador
        self.daño = daño
        self.efecto = efecto

    def probabilidad_trigger_estado(self):
        return self.probabilidad_afectar > random.random()
    
    def probabilidad_afectar_estado(self):
        return self.probabilidad_afectar > random.random()

quemado = Estado(nombre = 'Quemado', probabilidad_afectar = 0.5, probabilidad_trigger = 0.30, contador = 1, daño = 2, efecto = 'Reducir daño')
paralizado = Estado(nombre = 'Paralizado', probabilidad_afectar = 0.5, probabilidad_trigger = 0.30, contador = 1, efecto = 'Stun')
veneno = Estado(nombre = 'Veneno', probabilidad_afectar = 0.5, probabilidad_trigger = 0.30, contador = 1, daño = 5)

efectos = ['Reducir daño', 'Stun']

# _________________________________________________________________________________________________________________________

# CLASE DE ATAQUE
class Ataque: 
    contador_id = 1
    # lista_ataques_totales = []    

    def __init__(self, nombre: str, daño: int, empatia: int, estado: str = None, enfado: int = None):
        self.id = Ataque.contador_id  # Asigna el id actual y luego incrementa el contador
        Ataque.contador_id += 1
        self.nombre = nombre
        self.daño = daño
        self.empatia = empatia
        self.estado = estado
        self.enfado = enfado
        # self.lista_ataques_totales.append(Ataque)

    def atacar_1(self):
        return f"{self.nombre} hace {self.daño} de daño."

    def agrega_estado(self, estado):
        pass

    def get_lista_ataques_totales(self):
        return self.lista_ataques_totales

# _________________________________________________________________________________________________________________________

# CLASE DEL PROTA
class AtaqueProta(Ataque):

    arg_razonable = []
    acc_amistosa = []
    arg_cutre = []
    arg_toxico = []

    def __init__(self, nombre: str, daño: int, empatia: int, categoria: str, nivel: int = 0, estado: str = None, enfado: int = None):
        super().__init__(nombre, daño, empatia, categoria, estado)
        self.nivel = nivel
        self.categoria = categoria

    def __str__(self):
        return f"Ataque: {self.nombre}, Daño: {self.daño}, Empatía: {self.empatia}, Categoria: {self.categoria}, Nivel: {self.nivel}"    


# PROTA - CREAR LISTA DE ATAQUES DESORDENADA
def lista_ataques_desordenada():
    lista_ataques = [
    AtaqueProta(nombre = '"Tienes Razón 000"', daño = 0.5, empatia = 10, categoria = 'arg_razonable', nivel = 0, estado = quemado),
    AtaqueProta(nombre = '"No 000"', daño = 0.5, empatia = 10, categoria = 'arg_cutre', nivel = 0, estado = paralizado),
    AtaqueProta(nombre = '"tóxico man 000"', daño = 0.5, empatia = 10, categoria = 'arg_toxico', nivel = 0, estado = veneno),
    AtaqueProta(nombre = '"vamos al cine 000"', daño = 0.5, empatia = 10, categoria = 'acc_amistosa', nivel = 0, estado = quemado),
    AtaqueProta(nombre = '"Tienes Razón 111"', daño = 0.5, empatia = 10, categoria = 'arg_razonable', nivel = 1, estado = paralizado),
    AtaqueProta(nombre = '"No 000"', daño = 0.5, empatia = 10, categoria = 'arg_cutre', nivel = 1, estado = veneno),
    AtaqueProta(nombre = '"tóxico man 111"', daño = 0.5, empatia = 10, categoria = 'arg_toxico', nivel = 1, estado = quemado),
    AtaqueProta(nombre = '"vamos al cine 111"', daño = 0.5, empatia = 10, categoria = 'acc_amistosa', nivel = 1, estado = paralizado),
    AtaqueProta(nombre = '"Tienes Razón 222"', daño = 0.5, empatia = 10, categoria = 'arg_razonable', nivel = 2, estado = veneno),
    AtaqueProta(nombre = '"No 222"', daño = 0.5, empatia = 10, categoria = 'arg_cutre', nivel = 2, estado = quemado),
    AtaqueProta(nombre = '"tóxico man 222"', daño = 0.5, empatia = 10, categoria = 'arg_toxico', nivel = 2, estado = paralizado),
    AtaqueProta(nombre = '"vamos al cine 222"', daño = 0.5, empatia = 10, categoria = 'acc_amistosa', nivel = 2, estado = veneno),
    AtaqueProta(nombre = '"Tienes Razón 333"', daño = 0.5, empatia = 10, categoria = 'arg_razonable', nivel = 3, estado = quemado),
    AtaqueProta(nombre = '"No 333"', daño = 0.5, empatia = 10, categoria = 'arg_cutre', nivel = 3, estado = paralizado),
    AtaqueProta(nombre = '"tóxico man 333"', daño = 0.5, empatia = 10, categoria = 'arg_toxico', nivel = 3, estado = veneno),
    AtaqueProta(nombre = '"vamos al cine 333"', daño = 0.5, empatia = 10, categoria = 'acc_amistosa', nivel = 3, estado = paralizado),
    ]

    random.shuffle(lista_ataques) 
    return lista_ataques

# PROTA - CREAR GENERADOR DE ATAQUES POR NIVEL
def crear_ataque_nivel(nivel): 
    for generador_clase in list(generador_clase for generador_clase in lista_ataques_prota if generador_clase.nivel == nivel):
        if generador_clase in lista_ataques_utilizados:
            continue
        lista_ataques_utilizados.append(generador_clase)
        yield generador_clase

# PROTA - SELECCIONAR NUEVO ATAQUE
def seleccionar_nuevo_ataque(nivel):
    generador_clase = crear_ataque_nivel(nivel)
    if nivel == 0: 
        añadir_habilidad_categoria(next(generador_clase))
    else:
        clase1 = next(generador_clase)
        clase2 = next(generador_clase)
        opcion_escogida = input(f'''¿Qué habilidad escoges?:
                - 1. {clase1}
                - 2. {clase2}
                ''')
        if opcion_escogida == '1':
            lista_ataques_utilizados.append(clase1)
            añadir_habilidad_categoria(clase1)
            print(f'Muy bien, has añadido la habilidad {clase1.nombre} en la categoría {clase1.categoria}')
        elif opcion_escogida == '2':
            lista_ataques_utilizados.append(clase2)
            añadir_habilidad_categoria(clase2)
            print(f'\nMuy bien, has añadido la habilidad {clase2.nombre} en la categoría {clase2.categoria}')

# PROTA - AÑADIR HABILIDAD A LA CATEGORÍA 
def añadir_habilidad_categoria(generador):
    categoria = generador.categoria
    if categoria == 'arg_cutre':
        AtaqueProta.arg_cutre.append(generador)
    elif categoria == 'arg_razonable':
        AtaqueProta.arg_razonable.append(generador)
    elif categoria == 'arg_toxico':
        AtaqueProta.arg_toxico.append(generador)
    elif categoria == 'acc_amistosa':
        AtaqueProta.acc_amistosa.append(generador)
    

# PROTA - LISTA DE ATAQUES DESORDENADA
lista_ataques_prota = lista_ataques_desordenada()
lista_ataques_utilizados = []

# _________________________________________________________________________________________________________________________

# CLASE DEL BOSS
class AtaqueBoss(Ataque):

    lista_ataques_boss = []

    def __init__(self, nombre: str, daño: int, nivel: int = 0, empatia: int = None, estado: str = None, enfado: int = None):
        super().__init__(nombre, daño, estado, empatia, enfado)
        self.nivel = nivel
        
    def __str__(self):
        return f"Ataque: {self.nombre}, Daño: {self.daño}, Empatía: {self.empatia}, Nivel: {self.nivel}"
    

# BOSS - CREAR LISTA DE ATAQUES BOSS DESORDENADA
def lista_ataques_boss_desordenada():
    lista_ataques = [
    AtaqueBoss(nombre = '"Tú sabrás 00"', daño = 0.5, empatia = 10, nivel = 0, estado = quemado),
    AtaqueBoss(nombre = '"Haz lo que quieras 00"', daño = 0.5, empatia = 10, nivel = 0, estado = quemado),
    AtaqueBoss(nombre = '"tóxico BOSS 00"', daño = 0.5, empatia = 10, nivel = 0, estado = paralizado),
    AtaqueBoss(nombre = '"no me hables 00"', daño = 0.5, empatia = 10, nivel = 0, estado = paralizado),
    # AtaqueBoss('"Tú sabrás 11"', 2, -10, 'arg_toxico', 1),
    # AtaqueBoss('"Haz lo que quieras 11"', 1.5, 5, 'acc_amistosa', 1),
    # AtaqueBoss('"tóxico BOSS 11"', 1.5, 5, 'acc_amistosa', 1),
    # AtaqueBoss('"Tú sabrás 22"', 2, -10, 'arg_toxico', 2),
    # AtaqueBoss('"Haz lo que quieras 22"', 1.5, 5, 'acc_amistosa', 2),
    # AtaqueBoss('"Tú sabrás 33"', 1, -5, 'arg_cutre', 3),
    # AtaqueBoss('"Haz lo que quieras 33"', 1, -5, 'arg_cutre', 3)
    ]

    random.shuffle(lista_ataques) 
    return lista_ataques

def crear_ataque_nivel_boss(nivel): 
    for generador_clase in list(generador_clase for generador_clase in lista_ataques_boss if generador_clase.nivel == nivel):
        if generador_clase in lista_ataques_boss_utilizados:
            continue
        lista_ataques_boss_utilizados.append(generador_clase)
        yield generador_clase

def seleccionar_nuevo_ataque_boss(nivel):
    generador_clase = crear_ataque_nivel_boss(nivel)
    añadir_habilidad_lista_boss(next(generador_clase))

# BOSS - AÑADIR HABILIDAD A LA CATEGORÍA 
def añadir_habilidad_lista_boss(generador):
    AtaqueBoss.lista_ataques_boss.append(generador)
    # print(f'Se añadió la habilidad {generador.nombre} a la lista')

# BOSS - LISTA DE ATAQUES DESORDENADA
lista_ataques_boss = lista_ataques_boss_desordenada()
lista_ataques_boss_utilizados = []

# _________________________________________________________________________________________________________________________

# CLASE DEL ENEMIGO
class AtaqueEnemigo(Ataque):

    lista_ataques_enemigo = []

    def __init__(self, nombre: str, daño: int, nivel: int = 0, empatia: int =  None, estado: int = None, enfado: int = None):
        super().__init__(nombre, daño, empatia, estado, enfado)
        self.enfado = enfado
        self.nivel = nivel

    def __str__(self):
        return f"Ataque: {self.nombre}, Daño: {self.daño}, Categoria: {self.categoria}, Estado: {self.estado}"


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


    

