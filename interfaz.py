
import tkinter as tk
from tkinter import ttk
from automata import simular, validar_alfabeto


class InterfazSQL:
    def __init__(self, ventana):
        self.ventana = ventana

        ventana.title("Reconocedor de Inyecciones SQL")
        ventana.geometry("780x580")
        ventana.minsize(650, 480)

        # Titulo principal
        titulo = ttk.Label(
            ventana,
            text="Reconocedor de Inyecciones SQL",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        descripcion = ttk.Label(
            ventana,
            text="Simulacion de un Automata Finito Determinista"
        )
        descripcion.pack(pady=5)

        # Entrada del usuario
        ttk.Label(
            ventana,
            text="Ingrese la cadena que desea analizar:"
        ).pack(pady=10)

        self.entrada = ttk.Entry(ventana, width=65)
        self.entrada.pack(pady=5)

        # Botones
        contenedor_botones = ttk.Frame(ventana)
        contenedor_botones.pack(pady=15)

        ttk.Button(
            contenedor_botones,
            text="Analizar cadena",
            command=self.analizar
        ).pack(side="left", padx=10)

        ttk.Button(
            contenedor_botones,
            text="Limpiar",
            command=self.limpiar
        ).pack(side="left", padx=10)

        # Resultado
        self.resultado = ttk.Label(
            ventana,
            text="Esperando una cadena...",
            font=("Arial", 13, "bold")
        )
        self.resultado.pack(pady=10)

        # Titulo de la traza
        ttk.Label(
            ventana,
            text="Recorrido de estados del AFD:"
        ).pack(pady=5)

        # Area de texto
        self.area_traza = tk.Text(
            ventana,
            width=85,
            height=14,
            state="disabled"
        )
        self.area_traza.pack(padx=20, pady=10, fill="both", expand=True)

    def analizar(self):
        cadena = self.entrada.get()

           # Validar los caracteres antes de ejecutar el AFD
        if not validar_alfabeto(cadena):
            self.resultado.config(
                text="ENTRADA INVALIDA - Caracter fuera del alfabeto",
                foreground="orange"
            )

            self.area_traza.config(state="normal")
            self.area_traza.delete("1.0", tk.END)
            self.area_traza.insert(
                tk.END,
                "La cadena contiene caracteres fuera del alfabeto.\n"
                "Solo se permiten caracteres ASCII entre 32 y 126.\n"
                "El AFD no fue ejecutado."
            )
            self.area_traza.config(state="disabled")
            return

        aceptada, traza = simular(cadena)

        if aceptada:
            self.resultado.config(
                text="ACEPTADA - Patron SQL sospechoso detectado",
                foreground="red"
            )
        else:
            self.resultado.config(
                text="RECHAZADA - No se detecto el patron",
                foreground="green"
            )

        self.area_traza.config(state="normal")
        self.area_traza.delete("1.0", tk.END)

        self.area_traza.insert(tk.END, "Estado inicial: q0\n\n")

        for origen, simbolo, destino in traza:
            self.area_traza.insert(
                tk.END,
                f"q{origen} -- {simbolo!r} --> q{destino}\n"
            )

        self.area_traza.config(state="disabled")

    def limpiar(self):
        self.entrada.delete(0, tk.END)
        self.resultado.config(
            text="Esperando una cadena...",
            foreground="black"
        )

        self.area_traza.config(state="normal")
        self.area_traza.delete("1.0", tk.END)
        self.area_traza.config(state="disabled")
