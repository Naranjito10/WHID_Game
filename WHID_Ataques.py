import random

class Estado: 
    def __init__(self, nombre: str, probabilidad_afectar: int, probabilidad_trigger: int, contador: int, daño: int = 0, efecto: str = ''):
        self.nombre = nombre
        self.probabilidad_afectar = probabilidad_afectar
        self.probabilidad_trigger = probabilidad_trigger
        self.contador = contador
        self.daño = daño
        self.efecto = efecto

    def __str__(self):
        return f"Nombre: {self.nombre}, Probabilidad de trigger: {self.probabilidad_trigger}, Contador: {self.contador}, Daño: {self.daño}, Efecto: {self.efecto}"
    
    def probabilidad_afectar_estado(self):
        numero_aleatorio = random.random()
        return self.probabilidad_afectar > numero_aleatorio

    def probabilidad_trigger_estado(self):
        numero_aleatorio = random.random()
        print(numero_aleatorio)
        return self.probabilidad_afectar > numero_aleatorio
    
    def bajar_contador(self):
        if self.contador > 0:
            self.contador -= 1
            if self.contador == 0:
                return True
            return False
    
    def subir_contador(self):
        if self.efecto == 'Reducir daño' or self.efecto == 'Stun':
            self.contador += 1
        else:
            self.contador += 2

quemado = Estado(nombre = 'Quemado', probabilidad_afectar = 0.5, probabilidad_trigger = 0.30, contador = 1, daño = 2, efecto = 'Reducir daño')
paralizado = Estado(nombre = 'Paralizado', probabilidad_afectar = 0.5, probabilidad_trigger = 0.30, contador = 1, efecto = 'Stun')
veneno = Estado(nombre = 'Veneno', probabilidad_afectar = 0.5, probabilidad_trigger = 0.30, contador = 2, daño = 5, efecto = 'Veneno')
sofoque = Estado(nombre = 'Sofoque', probabilidad_afectar = 0.5, probabilidad_trigger = 0.30, contador = 1, daño = 5, efecto = 'Sofocado')
sin_estado = Estado(nombre = 'Sin estado', probabilidad_afectar = 0, probabilidad_trigger = 0, contador = 0, daño = 0, efecto = 'Sin efecto')

efectos = ['Reducir daño', 'Stun', 'Veneno', 'Sofocado']

# _________________________________________________________________________________________________________________________

# CLASE DE ATAQUE
class Ataque: 
    contador_id = 1
    # lista_ataques_totales = []    

    def __init__(self, nombre: str, daño: int, empatia: int, estado: str = sin_estado, enfado: int = 0):
        self.id = Ataque.contador_id  # Asigna el id actual y luego incrementa el contador
        Ataque.contador_id += 1
        self.nombre = nombre
        self.daño = daño
        self.empatia = empatia
        self.estado = estado
        self.enfado = enfado
        # self.lista_ataques_totales.append(Ataque)

    def get_lista_ataques_totales(self):
        return self.lista_ataques_totales

# _________________________________________________________________________________________________________________________

# CLASE DEL PROTA
class AtaqueProta(Ataque):

    arg_razonable = []
    acc_amistosa = []
    arg_cutre = []
    arg_toxico = []

    def __init__(self, nombre: str, daño: int, empatia: int, categoria: str, nivel: int = 0, estado: str = '', enfado: int = 0):
        super().__init__(nombre, daño, empatia, estado, enfado)
        self.nivel = nivel
        self.categoria = categoria

    def __str__(self):
        return f"Ataque: {self.nombre}, Daño: {self.daño}, Empatía: {self.empatia}, Categoria: {self.categoria}, Estado: {self.estado.nombre}"    


# PROTA - CREAR LISTA DE ATAQUES DESORDENADA
def lista_ataques_desordenada():
    lista_ataques = [
    AtaqueProta(nombre = '"Entiendo que estés preocupada, pero dime por favor qué está sucediendo para poder ayudarte”', daño = 0.5, empatia = 5, categoria = 'arg_razonable', nivel = 0, estado = quemado, enfado = 0),
    AtaqueProta(nombre = '“No sé qué he hecho”', daño = 0.5, empatia = 0, categoria = 'arg_cutre', nivel = 0, estado = paralizado, enfado = 0),
    AtaqueProta(nombre = '“Creo que es culpa tuya”', daño = 1, empatia = -5, categoria = 'arg_toxico', nivel = 0, estado = veneno, enfado = 0),
    AtaqueProta(nombre = '"Apoyas su argumento amistosamente"', daño = 0.5, empatia = 10, categoria = 'acc_amistosa', nivel = 0, estado = quemado, enfado = 0),
    AtaqueProta(nombre = '"“Resultaría más sencillo resolver este problema si me dijeras de donde viene el enfado”"', daño = 1, empatia = 10, categoria = 'arg_razonable', nivel = 1, estado = paralizado, enfado = 1),
    AtaqueProta(nombre = '"Creo que no he hecho nada mal"', daño = 1, empatia = 10, categoria = 'arg_cutre', nivel = 1, estado = veneno, enfado = 2),
    AtaqueProta(nombre = '"“¿Estás segura de lo que estás diciendo?”"', daño = 1, empatia = 10, categoria = 'arg_toxico', nivel = 1, estado = quemado, enfado = 6),
    AtaqueProta(nombre = '"Escuchas activamente"', daño = 1, empatia = 10, categoria = 'acc_amistosa', nivel = 1, estado = paralizado, enfado = 0),
    AtaqueProta(nombre = '"Tienes Razón 222"', daño = 2, empatia = 10, categoria = 'arg_razonable', nivel = 2, estado = veneno, enfado = 0),
    AtaqueProta(nombre = '"No 222"', daño = 2, empatia = 10, categoria = 'arg_cutre', nivel = 2, estado = quemado, enfado = 2),
    AtaqueProta(nombre = '"tóxico man 222"', daño = 2, empatia = 10, categoria = 'arg_toxico', nivel = 2, estado = paralizado, enfado = 8),
    AtaqueProta(nombre = '"vamos al cine 222"', daño = 2, empatia = 10, categoria = 'acc_amistosa', nivel = 2, estado = veneno, enfado = 0),
    AtaqueProta(nombre = '"Tienes Razón 333"', daño = 3, empatia = 10, categoria = 'arg_razonable', nivel = 3, estado = quemado, enfado = 0),
    AtaqueProta(nombre = '"No 333"', daño = 3, empatia = 10, categoria = 'arg_cutre', nivel = 3, estado = paralizado, enfado = 4),
    AtaqueProta(nombre = '"tóxico man 333"', daño = 3, empatia = 10, categoria = 'arg_toxico', nivel = 3, estado = veneno, enfado = 10),
    AtaqueProta(nombre = '"vamos al cine 333"', daño = 3, empatia = 10, categoria = 'acc_amistosa', nivel = 3, estado = paralizado, enfado = 0)
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
        opcion_escogida = input(f'''¿Qué habilidad escoges?:\n
                - 1. {clase1}
                - 2. {clase2}
                \nEscoge tu respuesta: ''')

        if opcion_escogida == '1':
            lista_ataques_utilizados.append(clase1)
            añadir_habilidad_categoria(clase1)
            print(f'Muy bien, has añadido la habilidad {clase1.nombre} en la categoría {clase1.categoria}')

        elif opcion_escogida == '2':
            lista_ataques_utilizados.append(clase2)
            añadir_habilidad_categoria(clase2)
            print(f'Muy bien, has añadido la habilidad {clase2.nombre} en la categoría {clase2.categoria}')

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

    def __init__(self, nombre: str, daño: int, empatia: int = 0, nivel: int = 0, estado: str = '', enfado: int = 0):
        super().__init__(nombre, daño, empatia, estado, enfado)
        self.nivel = nivel
        
    def __str__(self):
        return f"Ataque: {self.nombre}, Daño: {self.daño}, Empatía: {self.empatia}, Nivel: {self.nivel}, PENE.Estado: {self.estado.nombre}"
    
# BOSS - CREAR LISTA DE ATAQUES BOSS DESORDENADA
def lista_ataques_boss_desordenada():
    lista_ataques = [
    AtaqueBoss(nombre = '"Tú sabrás 00"', daño = 0.5, empatia = 10, nivel = 0, estado = quemado, enfado = 0),
    AtaqueBoss(nombre = '"Haz lo que quieras 00"', daño = 0.5, empatia = 10, nivel = 0, estado = quemado, enfado = 0),
    AtaqueBoss(nombre = '"tóxico BOSS 00"', daño = 0.5, empatia = 10, nivel = 0, estado = paralizado, enfado = 0),
    AtaqueBoss(nombre = '"no me hables 00"', daño = 0.5, empatia = 10, nivel = 0, estado = paralizado, enfado = 0),
    AtaqueBoss(nombre = '"Tú sabrás 11"', daño = 0.5, empatia = 10, nivel = 1, estado = quemado, enfado = 0),
    AtaqueBoss(nombre = '"Haz lo que quieras 11"', daño = 0.5, empatia = 10, nivel = 1, estado = quemado, enfado = 0),
    AtaqueBoss(nombre = '"tóxico BOSS 11"', daño = 0.5, empatia = 10, nivel = 1, estado = paralizado, enfado = 0),
    AtaqueBoss(nombre = '"no me hables 11"', daño = 0.5, empatia = 10, nivel = 1, estado = paralizado, enfado = 0),
    AtaqueBoss(nombre = '"Tú sabrás 22"', daño = 0.5, empatia = 10, nivel = 2, estado = quemado, enfado = 0),
    AtaqueBoss(nombre = '"Haz lo que quieras 22"', daño = 0.5, empatia = 10, nivel = 2, estado = quemado, enfado = 0),
    AtaqueBoss(nombre = '"tóxico BOSS 22"', daño = 0.5, empatia = 10, nivel = 2, estado = paralizado, enfado = 0),
    AtaqueBoss(nombre = '"no me hables 22"', daño = 0.5, empatia = 10, nivel = 2, estado = paralizado, enfado = 0),
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

    def __init__(self, nombre: str, daño: int, nivel: int = 0, enfado: int = 0, estado: str = '', empatia: int = 0):
        super().__init__(nombre, daño, empatia, estado, enfado)
        self.nivel = nivel

    def __str__(self):
        return f"Ataque: {self.nombre}, Daño: {self.daño}, Estado: {self.estado}"

stun_activado = Ataque(nombre = 'stun_activado', daño = 0, empatia = 0, estado = sin_estado, enfado = 0)

# OTROS

# arg_razonables = [{'id': 1, 
#                   'arg_1': 'Tienes razón', 
#                   'Fuerza': 5,
#                   'Categoria': 'arg_razonables'}, 
#                   {'id': 2, 
#                   'arg_1': 'Lo siento', 
#                   'Fuerza': 10,
#                   'Categoria': 'arg_razonables'},
#                   {'id': 3, 
#                   'arg_1': 'Eres la mejor', 
#                   'Fuerza': 5,
#                   'Categoria': 'arg_razonables'}, 
#                   {'id': 4, 
#                   'arg_1': 'Dime porfa que pasó', 
#                   'Fuerza': 10,
#                   'Categoria': 'arg_razonables'}]

# acc_amistosa = [{'id': 1, 
#                   'arg_1': 'Amo al cine', 
#                   'Fuerza': 5,
#                   'Categoria': 'acc_amistosa'}, 
#                   {'id': 2, 
#                   'arg_1': 'Amo al teatro', 
#                   'Fuerza': 10,
#                   'Categoria': 'acc_amistosa'},
#                   {'id': 3, 
#                   'arg_1': 'Compramos comida?', 
#                   'Fuerza': 5,
#                   'Categoria': 'acc_amistosa'}, 
#                   {'id': 4, 
#                   'arg_1': 'Quieres chuches?', 
#                   'Fuerza': 10,
#                   'Categoria': 'acc_amistosa'}]

# ata_toxico = [{'id': 1, 
#                   'arg_1': 'Eres tú', 
#                   'Fuerza': 5,
#                   'Categoria': 'ata_toxico',
#                   'Estado': 'Quemado',
#                   'Probabilidad_efecto': 0.30}, 
#                   {'id': 2, 
#                   'arg_1': 'Soy así', 
#                   'Fuerza': 10,
#                   'Categoria': 'ata_toxico',
#                   'Estado': 'Congelado',
#                   'Probabilidad_efecto': 0.30},
#                   {'id': 3, 
#                   'arg_1': 'Tu culpa', 
#                   'Fuerza': 5,
#                   'Categoria': 'ata_toxico',
#                   'Estado': 'Paralizado',
#                   'Probabilidad_efecto': 0.30}, 
#                   {'id': 4, 
#                   'arg_1': 'Mi padre me hizo asi', 
#                   'Fuerza': 10,
#                   'Categoria': 'ata_toxico',
#                   'Estado': 'Congelado',
#                   'Probabilidad_efecto': 0.30}]

# arg_cutre = [{'id': 1, 
#                   'arg_1': 'El qué?', 
#                   'Fuerza': 5,
#                   'Categoria': 'arg_cutre'}, 
#                   {'id': 2, 
#                   'arg_1': 'Yo?', 
#                   'Fuerza': 10,
#                   'Categoria': 'arg_cutre'},
#                   {'id': 3, 
#                   'arg_1': 'Nosé', 
#                   'Fuerza': 5,
#                   'Categoria': 'arg_cutre'}, 
#                   {'id': 4, 
#                   'arg_1': 'De qué hablas?', 
#                   'Fuerza': 10,
#                   'Categoria': 'arg_cutre'}]


    

