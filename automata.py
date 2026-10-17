
# AFD - Reconocedor de inyecciones SQL básicas


ESTADO_INICIAL = 0
ESTADO_FINAL = 12


TRANSICIONES = {
    0: {"'": 1},
    1: {" ": 2},
    2: {"-": 3, "O": 4},
    3: {"-": 12},
    4: {"R": 5},
    5: {" ": 6},
    6: {"1": 7},
    7: {"=": 8},
    8: {"1": 9},
    9: {" ": 10},
    10: {"-": 11},
    11: {"-": 12}
}

def delta(estado, simbolo):
   
    if estado == ESTADO_FINAL:
        return ESTADO_FINAL

   
    if simbolo in TRANSICIONES[estado]:
        return TRANSICIONES[estado][simbolo]

   
    if simbolo == "'":
        return 1

  
    return ESTADO_INICIAL


def validar_alfabeto(cadena):
    for simbolo in cadena:
        if not (32 <= ord(simbolo) <= 126):
            return False

    return True


def simular(cadena):
    estado = ESTADO_INICIAL
    traza = []

    if not validar_alfabeto(cadena):
        return False, traza

    for simbolo in cadena:
        siguiente = delta(estado, simbolo)

        traza.append((estado, simbolo, siguiente))

        estado = siguiente

    aceptada = estado == ESTADO_FINAL

    return aceptada, traza
