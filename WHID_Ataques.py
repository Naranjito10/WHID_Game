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
        print(f'AFECTAR. Este es el número aleatorio: {numero_aleatorio}')
        print(f'AFECTAR. Esta es la posibilidad de trigger: {self.probabilidad_afectar}')
        return self.probabilidad_afectar > numero_aleatorio

    def probabilidad_trigger_estado(self):
        numero_aleatorio = random.random()
        print(f'TRIGGER. Este es el número aleatorio: {numero_aleatorio}')
        print(f'TRIGGER. Esta es la posibilidad de trigger: {self.probabilidad_trigger}')
        return self.probabilidad_trigger > numero_aleatorio
    
    def subir_contador(self):
        if self.efecto == 'Reducir daño' or self.efecto == 'Stun':
            self.contador += 1
            print(f'El contador de {self.nombre} es {self.contador}')
        else:
            self.contador += 2
            print(f'El contador de {self.nombre} es {self.contador}')

# ESTADOS Y ATAQUES
quemado_enemigos = Estado(nombre = 'Quemado', probabilidad_afectar = 0.9, probabilidad_trigger = 0.30, contador = 1, daño = 2, efecto = 'Reducir daño')
paralizado_enemigos = Estado(nombre = 'Paralizado', probabilidad_afectar = 0.7, probabilidad_trigger = 0.30, contador = 1, efecto = 'Stun')
envenenado_enemigos = Estado(nombre = 'Envenenado', probabilidad_afectar = 0.9, probabilidad_trigger = 0.30, contador = 1, daño = 5, efecto = 'Veneno')
sofocado_enemigos = Estado(nombre = 'Sofocado', probabilidad_afectar = 0.8, probabilidad_trigger = 0.30, contador = 1, daño = 5, efecto = 'Bajar armadura')

quemado_prota = Estado(nombre = 'Quemado', probabilidad_afectar = 0.9, probabilidad_trigger = 0.30, contador = 1, daño = 2, efecto = 'Reducir daño')
paralizado_prota = Estado(nombre = 'Paralizado', probabilidad_afectar = 0.7, probabilidad_trigger = 0.30, contador = 1, efecto = 'Stun')
envenenado_prota = Estado(nombre = 'Envenenado', probabilidad_afectar = 0.9, probabilidad_trigger = 0.30, contador = 1, daño = 5, efecto = 'Veneno')
sofocado_prota = Estado(nombre = 'Sofocado', probabilidad_afectar = 0.8, probabilidad_trigger = 0.30, contador = 1, daño = 5, efecto = 'Bajar armadura')

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
        return f'''Ataque: {self.nombre}
        (Daño: {self.daño}, Empatía: {self.empatia}, Categoría: {self.categoria}, Estado: {self.estado.nombre})'''   


# PROTA - CREAR LISTA DE ATAQUES DESORDENADA
def lista_ataques_desordenada():
    lista_ataques = [
    # NIVEL 0
    AtaqueProta(nombre = '"Entiendo que estés preocupada, pero dime por favor qué está sucediendo para poder ayudarte."', 
                daño = 0.5, 
                empatia = 5, 
                categoria = 'arg_razonable', 
                nivel = 0, 
                estado = quemado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"No sé qué he hecho.”', 
                daño = 0.5, 
                empatia = 0, 
                categoria = 'arg_cutre', 
                nivel = 0, 
                estado = paralizado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"Creo que es culpa tuya."', 
                daño = 1, 
                empatia = -5, 
                categoria = 'arg_toxico', 
                nivel = 0, 
                estado = envenenado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"Te escucho."', 
                daño = 0.5, 
                empatia = 10, 
                categoria = 'acc_amistosa', 
                nivel = 0, 
                estado = quemado_enemigos, 
                enfado = 0),
    # NIVEL 1
    AtaqueProta(nombre = '"Resultaría más sencillo resolver este problema si me dijeras de donde viene el enfado."', 
                daño = 1.5, 
                empatia = 10, 
                categoria = 'arg_razonable', 
                nivel = 1, 
                estado = paralizado_enemigos, 
                enfado = 1),
    AtaqueProta(nombre = '"Creo que no he hecho nada mal."', 
                daño = 2, 
                empatia = 10, 
                categoria = 'arg_cutre', 
                nivel = 1, 
                estado = envenenado_enemigos, 
                enfado = 2),
    AtaqueProta(nombre = '"¿Estás segura de lo que estás diciendo?"', 
                daño = 2.5, 
                empatia = 10, 
                categoria = 'arg_toxico', 
                nivel = 1, 
                estado = quemado_enemigos, 
                enfado = 6),
    AtaqueProta(nombre = '"Escuchas activamente."', 
                daño = 2, 
                empatia = 10, 
                categoria = 'acc_amistosa', 
                nivel = 1, 
                estado = paralizado_enemigos, 
                enfado = 0),
    # NIVEL 2
    AtaqueProta(nombre = '"Sé que a veces puedo parecer distante, pero quiero luchar para mejorar nuestra comunicación."', 
                daño = 2, 
                empatia = 10, 
                categoria = 'arg_razonable', 
                nivel = 2, 
                estado = envenenado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"Lo siento."', 
                daño = 2, 
                empatia = 0, 
                categoria = 'arg_cutre', 
                nivel = 2, 
                estado = quemado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"Sí cariño, tienes toooooda la razón.”', 
                daño = 3, 
                empatia = -10, 
                categoria = 'arg_toxico', 
                nivel = 2, 
                estado = envenenado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"¿Te gustaría pasar un tiempo especial juntos este fin de semana?"',
                daño = 2.5,
                empatia = 5,
                categoria = 'acc_amistosa',
                nivel = 2,
                estado = paralizado_enemigos,
                enfado = 0),
    # NIVEL 3
    AtaqueProta(nombre = '"No quería hacerte daño."', 
                daño = 2, 
                empatia = 0, 
                categoria = 'arg_cutre', 
                nivel = 3, 
                estado = paralizado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"Apoyas su argumento amistosamente."', 
                daño = 3, 
                empatia = 5, 
                categoria = 'acc_amistosa', 
                nivel = 3, 
                estado = quemado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"No me gusta que me hables así."',
                daño = 3.5, 
                empatia = -10, 
                categoria = 'arg_toxico', 
                nivel = 3, 
                estado = envenenado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"He notado que ha habido un cambio entre nosotros... ¿Hay algo en particular que te haya molestado?"',
                daño = 2,
                empatia = 10,
                categoria = 'arg_razonable',
                nivel = 3,
                estado = paralizado_enemigos,
                enfado = -8),
    # NIVEL 4
    AtaqueProta(nombre = '"Te quiero."', 
                daño = 2.5, 
                empatia = 10, 
                categoria = 'arg_cutre', 
                nivel = 4, 
                estado = quemado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"Repites lo que ha dicho la otra persona para demostrar que estás atento."',
                daño = 3.5,
                empatia = 15,
                categoria = 'acc_amistosa',
                nivel = 4,
                estado = paralizado_enemigos,
                enfado = 0),
    AtaqueProta(nombre = '"No entiendo por qué siempre encuentras algo de qué quejarte. "',
                daño = 4, 
                empatia = -10, 
                categoria = 'arg_toxico', 
                nivel = 4, 
                estado = envenenado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"¿Hacemos un puzzle juntos? Quiero hacer un esfuerzo adicional para fortalecer nuestra conexión."',
                daño = 2.5,
                empatia = 15,
                categoria = 'arg_razonable',
                nivel = 4,
                estado = paralizado_enemigos,
                enfado = 0),
    # NIVEL 5
    AtaqueProta(nombre = '"Nuestras decisiones impactan el futuro directamente. ¿Qué podemos hacer para mejorar nuestra relación a largo plazo?”"',
                daño = 3.5,
                empatia = 20,
                categoria = 'arg_razonable',
                nivel = 5,
                estado = paralizado_enemigos,
                enfado = 0),
    AtaqueProta(nombre = '"Me interesa entender mejor tu punto de vista. ¿Podrías explicarme más sobre tus experiencias y cómo llegaste a esa conclusión?"',
                daño = 4.5,
                empatia = 10,
                categoria = 'acc_amistosa',
                nivel = 5,
                estado = paralizado_enemigos,
                enfado = 0),
    AtaqueProta(nombre = '"Estuve revisando tu Whatsapp y parece que eres tú la que me debe una explicación… ¿Quién es "Paco Fontanero"?"',
                daño = 5.5, 
                empatia = -20, 
                categoria = 'arg_toxico', 
                nivel = 5, 
                estado = envenenado_enemigos, 
                enfado = 0),
    AtaqueProta(nombre = '"¡No sé de qué estás hablando!"',
                daño = 4.5,
                empatia = -5,
                categoria = 'arg_cutre',
                nivel = 5,
                estado = quemado_enemigos,
                enfado = 0)    
    ]

    random.shuffle(lista_ataques) 
    return lista_ataques

# PROTA - SELECCIÓN HABILIDADES PARA BORRAR
def seleccionar_habilidad_borrar():
    opcion_escogida = ''
    opcion1 = random.choice(AtaqueProta.arg_cutre)
    opcion2 = random.choice(AtaqueProta.arg_razonable)
    opcion3 = random.choice(AtaqueProta.arg_toxico)
    opcion4 = random.choice(AtaqueProta.acc_amistosa)
    while opcion_escogida not in ['1', '2', '3', '4']:
        try:
            opcion_escogida = input(f'''¿Qué habilidad quieres borrar?:\n
    - 1. {opcion1}
    - 2. {opcion2}
    - 3. {opcion3}
    - 4. {opcion4}
    \nEscoge tu respuesta: ''')
        except ValueError:
            print('Por favor, introduce un número.')

    if opcion_escogida == '1':
        AtaqueProta.arg_cutre.remove(opcion1)
        print(f'Muy bien, has borrado la habilidad {opcion1.nombre} en la categoría {opcion1.categoria}')

    elif opcion_escogida == '2':
        AtaqueProta.arg_razonable.remove(opcion2)
        print(f'Muy bien, has borrado la habilidad {opcion2.nombre} en la categoría {opcion2.categoria}')

    elif opcion_escogida == '3':
        AtaqueProta.arg_toxico.remove(opcion3)
        print(f'Muy bien, has borrado la habilidad {opcion3.nombre} en la categoría {opcion3.categoria}')
    
    elif opcion_escogida == '4':
        AtaqueProta.acc_amistosa.remove(opcion4)
    print(f'Muy bien, has borrado la habilidad {opcion4.nombre} en la categoría {opcion4.categoria}')

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
        opcion_escogida = ''
        while opcion_escogida != '1' and opcion_escogida != '2':
            try:
                opcion_escogida = input(f'''¿Qué habilidad escoges?:\n
    - 1. {clase1}
    - 2. {clase2}
    \nEscoge tu respuesta: ''')
            except ValueError:
                print('Por favor, introduce un número.')

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
    AtaqueBoss(nombre = '"Tú sabrás 00"', daño = 0.5, empatia = 0, nivel = 0, estado = envenenado_prota, enfado = 1),
    AtaqueBoss(nombre = '"Haz lo que quieras 00"', daño = 0.5, empatia = 0, nivel = 0, estado = envenenado_prota, enfado = 1),
    AtaqueBoss(nombre = '"tóxico BOSS 00"', daño = 0.5, empatia = 0, nivel = 0, estado = quemado_prota, enfado = 1),
    AtaqueBoss(nombre = '"no me hables 00"', daño = 0.5, empatia = 0, nivel = 0, estado = quemado_prota, enfado = 1),
    AtaqueBoss(nombre = '"Tú sabrás 11"', daño = 0.5, empatia = 0, nivel = 1, estado = envenenado_prota, enfado = 1),
    AtaqueBoss(nombre = '"Haz lo que quieras 11"', daño = 0.5, empatia = 0, nivel = 1, estado = envenenado_prota, enfado = 1),
    AtaqueBoss(nombre = '"tóxico BOSS 11"', daño = 0.5, empatia = 0, nivel = 1, estado = quemado_prota, enfado = 1),
    AtaqueBoss(nombre = '"no me hables 11"', daño = 0.5, empatia = 0, nivel = 1, estado = quemado_prota, enfado = 1),
    AtaqueBoss(nombre = '"Tú sabrás 22"', daño = 0.5, empatia = 0, nivel = 2, estado = sofocado_prota, enfado = 1),
    AtaqueBoss(nombre = '"Haz lo que quieras 22"', daño = 0.5, empatia = 0, nivel = 2, estado = sofocado_prota, enfado = 1),
    AtaqueBoss(nombre = '"tóxico BOSS 22"', daño = 0.5, empatia = 0, nivel = 2, estado = paralizado_prota, enfado = 1),
    AtaqueBoss(nombre = '"no me hables 22"', daño = 0.5, empatia = 0, nivel = 2, estado = paralizado_prota, enfado = 1),
    ]
    random.shuffle(lista_ataques) 
    return lista_ataques

# BOSS - CREAR GENERADOR DE ATAQUES POR NIVEL
def crear_ataque_nivel_boss(nivel): 
    for generador_clase in list(generador_clase for generador_clase in lista_ataques_boss if generador_clase.nivel == nivel):
        if generador_clase in lista_ataques_boss_utilizados:
            continue
        lista_ataques_boss_utilizados.append(generador_clase)
        yield generador_clase

# BOSS - SELECCIONAR NUEVO ATAQUE
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
