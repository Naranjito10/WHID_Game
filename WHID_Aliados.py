from WHID_Ataques import *

# ALIADOS
class Aliado():

    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __str__(self):
        return f'Nombre: {self.nombre}'

    def eleccion_personaje(self, personaje, novia):
        # El PADRE te da un consejo y te da una nueva habilidad
        if self.nombre == 'Padre':
            print(f'Tu padre te ofrece dos herramientas para mitigar el enfado de tu novia. ¿Cuál escoges?')
            seleccionar_nuevo_ataque(personaje.nivel)
            print('Tu padre te ha dado un par de consejos y te sientes más seguro de ti mismo')

        # La MADRE te da un consejo y te sube una
        elif self.nombre == 'Madre':
            print('Tu madre te explica que no es bueno discutir con tu novia, es mejor hablar las cosas tranquilamente')
            personaje.seleccionar_subida_caracteristicas()
            print('Tu madre siempre es sabia y te sientes más seguro de ti mismo')

        # La ABUELA te da de comer y te sube la energía y alguna característica
        elif self.nombre == 'Abuela':
            comida = '0'
            while comida not in ['1', '2', '3', '4']:
                try:
                    comida = input('''Tu abuela te pregunta que quieres para comer: \n         
    - 1. Lentejas (+20 energía)
    - 2. Tortilla (+10 empatía, +10 energía)
    - 3. Macarrones (+10 dialéctica, +10 energía)
    - 4. Pescado (+5 empatía, +5 dialéctica)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 4')

            if comida == '1':
                print('Tu abuela te ha hecho unas lentejas y te sientes más fuerte')
                personaje.energia += 20
            elif comida == '2':
                print('Tu abuela te ha hecho una tortilla y te sientes más fuerte')
                personaje.empatia += 10
                personaje.energia += 10
            elif comida == '3':
                print('Tu abuela te ha hecho unos macarrones y te sientes más fuerte')
                personaje.dialectica += 10
                personaje.energia += 10
            elif comida == '4':
                personaje.dialectica += 5
                personaje.empatia += 5
                print('Tu abuela te ha hecho pescado y te sientes más fuerte')
        
        # El ABUELO te cuenta una historia y te sube de nivel pero te baja la empatía y sube el enfado de tu novia
        elif self.nombre == 'Abuelo':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu abuelo te cuenta la historia de cuando era joven y tu abuela se enfadó muchísimo con él. 
    Qué lástima que sean tiempos tan distintos... ¿Quieres seguir sus consejos?:\n                        
    - 1. Sí (-15 empatía, +1 nivel)
    - 2. No (+20 energía)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Tu abuelo te ha contado una historia y te sientes más fuerte pero con ideas anticuadas.')
                personaje.empatia -= 10
                print(f'Ahora tu EMPATÍA es {personaje.empatia}.')
                personaje.subir_nivel(sobrante_experiencia = 0)
            elif eleccion == '2':
                print('Piensas que tu abuelo tiene ideas anticuadas y no le haces caso. Al menos te ha dado chuches.')
                personaje.energia += 20
                personaje.empatia += 5
                print(f'Ahora tu ENERGÍA es {personaje.energia} y tu EMPATÍA es {personaje.empatia}.')

        # El AMIGO te da un consejo y te sube la dialectica
        elif self.nombre == 'Amigo':
            print('Tu amigo intenta darte un consejo pero no se le ocurre nada. Al menos te ha dado un Sed Buy.')
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Si decides bebértelo, tu dialéctica subirá, pero tu empatía bajará. ¿Quieres bebértelo?\n
    - 1. Sí (+10 dialéctica, -10 empatía)
    - 2. No (No pasa nada)
    \n¿Qué haces?: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Te sientes más despierto y con más energía, tienes ganas de discutir.')
                personaje.dialectica += 10
                print(f'Ahora tu dialéctica es {personaje.dialectica}.')

        # Tu AMIGA te invita a su casa a ver una peli y te sube la energía y la empatía pero sube el enfado de tu novia
        elif self.nombre == 'Amiga':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Tu amiga quiere que te vayas a su casa a ver una peli para calmarte. ¿Aceptas?
    - 1. Sí
    - 2. No
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')

            if eleccion == '1':
                print('Veis Shreck y te sientes mucho más comprendido y con energía. Que pena que te vieron con tu amiga...')
                personaje.energia += 40
                personaje.paciencia += 2
                personaje.empatia += 1
                novia.enfado += 10
                print(f'Ahora tu ENERGÍA es {personaje.energia}, tu PACIENCIA es {personaje.paciencia} y tu empatía es {personaje.empatia}. Pero el enfado de tu novia ha subido a {novia.enfado}.')

            elif eleccion == '2':
                print('Tu amiga te dice que no te preocupes, que te va a ayudar a salir de esta.')
                personaje.dialectica += 5
                print(f'Ahora tu dialéctica es {personaje.dialectica}.')
        
        # Tu HERMANO te invita a jugar al futbol o a tomar unas cervezas
        elif self.nombre == 'Hermano':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Tu hermano te dice de hacer algo con él para que te distraigas. ¿Qué prefieres?\n                  
    - 1. Ir a jugar al futbol (-10 energía, +10 empatía)
    - 2. Ir a tomar unas cervezas (+20 energía, -5 dialéctica)
    \nTu respuesta: ''') 
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
  
            if eleccion == '1':
                print('El partido te ha cansado un poco pero te sientes más empático.')
                personaje.energia -= 10
                personaje.empatia += 10
                print(f'Ahora tu EMPATÍA es {personaje.empatia} y tu ENERGÍA es {personaje.energia}.')
            elif eleccion == '2':
                print('Te sientes achispado pero te cuesta algo vocalizar tus argumentos.')
                personaje.energia += 30
                personaje.dialectica -= 5
                print(f'Ahora tu dialéctica es {personaje.dialectica} y tu energía es {personaje.energia}.')
            
        # Tu HERMANA te invita a ir de compras o a un escape room
        elif self.nombre == 'Hermana':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''Tu hermana entiende perfectamente la situación y te da un abrazo. 
    Te ofrece un par de planes para desconectar:
                             
    - 1. Ir de compras (-10 energía, +5 empatía, +5 dialéctica)
    - 2. Ir a un Escape Room (-20 energía, +3 paciencia)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Te sientes más carismático.')
                personaje.energia -= 10
                personaje.empatia += 5
                personaje.dialectica += 5
                print(f'Ahora tu EMPATÍA es {personaje.empatia}, tu dialéctica es {personaje.dialectica} y tu ENERGÍA es {personaje.energia}.')
            elif eleccion == '2':
                print('Te sientes más tranquilo.')
                personaje.energia -= 20
                personaje.paciencia += 3
                print(f'Ahora tu PACIENCIA es {personaje.paciencia} y tu ENERGÍA es {personaje.energia}.')
        
        # Tu PERRO te da un lametón y te sube la paciencia o la empatía
        elif self.nombre == 'Perro':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu perro te da un lametón en la cara ya que te ve triste. ¿Qué haces?\n
    - 1. Lo sacas a pasear. (+2 paciencia)
    - 2. Lo acaricias y juegas con él. (+5 empatía)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Dar una vuelta con tu perro te ha relajado.')
                personaje.paciencia += 2
                print(f'Ahora tu ENERGÍA es {personaje.energia}.')
            elif eleccion == '2':
                print('Pasar un rato con tu perro te ha hecho sentir más alegre.')
                personaje.empatia += 5
                print(f'Ahora tu ENERGÍA es {personaje.energia}.')

        elif self.nombre == 'Gato':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu gato está acurrucado en tu cama. ¿Qué haces?\n
    - 1. Lo agarras y lo mimas hasta que te araña por pesado. (-10 energia, +10 empatía)
    - 2. Sacas un cordel y juegas con él. (+15 energia, +1 empatía)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Tu gato te ha arañado y pero ha merecido la pena')
                personaje.energia -= 10
                personaje.empatia += 10
                print(f'Ahora tu ENERGÍA es {personaje.energia} y tu EMPATÍA es {personaje.empatia}.')
            elif eleccion == '2':
                print('Tu gato se ha cansado y se ha dormido pero tú has recuperado fuerzas.')
                personaje.energia += 15
                personaje.empatia += 1
                print(f'Ahora tu ENERGÍA es {personaje.energia} y tu EMPATÍA es {personaje.empatia}.')
                
        elif self.nombre == 'Compañero de clase':
            print('Tu compañero te pregunta qué tal estás y si tienes papel. ¿Qué le dices?')
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu compañero bromea diciéndote que tu novia está preciosa, que si se la prestas para "calmarla". ¿Qué haces?\n
    - 1. Te peleas con él. (Borras una habilidad de tu kit)
    - 2. Sudas de su cara. (Augmentas tu PACIENCIA en 2)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('De un puñetazo que recibes te olvidas de como argumentar correctamente.')
                seleccionar_habilidad_borrar()
            elif eleccion == '2':
                print('Tu autocontrol es envidiable.')
                personaje.paciencia += 2
                print(f'Ahora tu PACIENCIA es {personaje.paciencia}.')
        
        elif self.nombre == 'Compañera de clase':
            eleccion = '0'
            while eleccion not in ['1', '2']:
                try:
                    eleccion = input('''\nTu compañera te dice de acompañarla al baño de chicas para contarte un secretito. ¿Qué le dices?\n
    - 1. Aceptas. (Sorpresa)
    - 2. Le dices que no porque desconfias de sus intenciones. (Sorpresa)
    \nTu respuesta: ''')
                except ValueError:
                    print('Debes escoger un número entre 1 y 2')
            if eleccion == '1':
                print('Tu novia te ha visto y ha pensado que te estabas enrollando con ella. Su ENFADO ha subido. Además, tu compañera te ha contado un secreto que no te importaba.')
                novia.enfado += 10
                personaje.energia -= 20
                personaje.paciencia += 2
                print(f'Ahora tu energia es {personaje.energia} y tu PACIENCIA es {personaje.paciencia}. El ENFADO de tu novia es {novia.enfado}.')
            elif eleccion == '2':
                print('Tu novia te ha visto y ha pensado que eres un buen chico. Su ENFADO ha bajado.')
                novia.enfado -= 10
                print(f'Ahora el ENFADO de tu novia es {novia.enfado}.')
        
