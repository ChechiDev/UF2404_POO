import sys
import os

"""
Escribe un programa que muestre un carácter usado como argumento.
El prototipo del main deberá ser el siguiente:
def main():
		char = sys.argv[1]

El prototipo de la función deberá ser el siguiente:
def print_char(char):

Debes incluir el módulo sys:
import sys

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""


def print_char(char):
    """
    Imprime el carácter recibido como argumento.

    Arg: char (str): El carácter a imprimir.

    Return: str: print(char)
    """
    os.system("cls")
    return print(char)

def main():
    if len(sys.argv) == 2:
        try:
            char = str(sys.argv[1] if len(sys.argv) > 1 else False)

            print_char(char)


        except ValueError:
            print("Error: El argumento debe ser un carácter válido.")

    else:
        print("Uso: python print_char.py <carácter>")


if __name__ == "__main__":
    main()