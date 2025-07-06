import sys
import os
import string

"""
Escribe un programa que muestre el alfabeto en minúsculas en una sola línea, en orden creciente, empezando en la letra “a”.
El prototipo del main deberá ser el siguiente:

def main():

El prototipo de la función deberá ser el siguiente:

def print_alphabet():

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos

if __name__ == "__main__":
    main()
"""

def print_alphabet():
    """
    Imprime el alfabeto en minúsculas en una sola línea, en orden creciente.
    """
    os.system("cls")
    return print(string.ascii_lowercase)


def main():
    if len(sys.argv) == 1:
        print_alphabet()

    else:
        print("Uso: python print_alphabet.py")


if __name__ == "__main__":
    main()