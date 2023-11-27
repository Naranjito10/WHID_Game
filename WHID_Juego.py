from WHID_Clases import *

primo = Personaje('Erik', 40, 60, 10, 5)
padre = Personaje('Juan', 30, 50, 1, 10)
print(padre)

resultado_ataque = primo.atacar(10)
resultado_defensa = padre.defender(resultado_ataque)
print(resultado_defensa)