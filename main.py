
import tkinter as tk
from interfaz import InterfazSQL


def main():
    ventana = tk.Tk()
    InterfazSQL(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
