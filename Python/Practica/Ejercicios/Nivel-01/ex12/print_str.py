import sys

"""
Escribe un programa que muestre uno a uno (con un salto de línea) en la pantalla los caracteres de un string.
El prototipo del main deberá ser el siguiente:
def main():

		string = sys.argv[1]

El prototipo de la función deberá ser el siguiente:
def print_str(string):

Debes incluir el módulo sys:
import sys

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""


def print_str(s):
    """
    Muestra uno a uno (con un salto de línea) en la pantalla los caracteres de un string
    Arg1: str : Cadena de texto.
    """

    for i in s:
        print(i + "\n")


def main():
    if len(sys.argv) == 2:

        try:
            s = str(sys.argv[1])
            print_str(s)

        except ValueError:
            print("Error: El argumento debe ser una cadena de texto.")
            return

    else:
        print("Uso: python print_str.py <cadena>")
        return

if __name__ == "__main__":
    main()