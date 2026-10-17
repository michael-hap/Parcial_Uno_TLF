
from automata import simular

# Cada prueba contiene:
# (cadena, resultado_esperado)

casos_prueba = [
    # Cadenas que deben ser aceptadas
    ("' --", True),
    ("admin' --", True),
    ("usuario' OR 1=1 --", True),
    ("123' OR 1=1 --", True),
    ("abc' --xyz", True),

    # Cadenas que deben ser rechazadas
    ("admin123", False),
    ("usuario", False),
    ("OR 1=1", False),
    ("admin' OR 1=2 --", False),
    ("admin' OR 1=1", False),

    # Pruebas adicionales
    ("", False),
    ("abc' O' OR 1=1 --", True),
    ("' -' --", True),
    ("' OR 1=1 -", False),
    ("' --' OR 1=1 --", True),

    ("niño' --", False),
    ("café' OR 1=1 --", False),
    ("admin' --\n", False),
    ("admin' --", True)
]


def ejecutar_pruebas():
    correctas = 0

    for numero, (cadena, esperado) in enumerate(casos_prueba, 1):
        obtenido, traza = simular(cadena)

        if obtenido == esperado:
            resultado = "CORRECTA"
            correctas += 1
        else:
            resultado = "ERROR"

        print(f"\nPrueba {numero}: {cadena!r}")
        print(f"Esperado: {esperado}")
        print(f"Obtenido: {obtenido}")
        print(f"Resultado: {resultado}")

    print("\nRESUMEN")
    print(f"Pruebas correctas: {correctas}/{len(casos_prueba)}")


if __name__ == "__main__":
    ejecutar_pruebas()
