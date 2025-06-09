import sys
import os
import string

"""
Escribe un programa que muestre el alfabeto en Mayúsculas en una sola línea, en orden decreciente, empezando en la letra “z”.
El prototipo del main deberá ser el siguiente:
def main():

El prototipo de la función deberá ser el siguiente:
def print_reverse_alphabet():

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""

def print_reverse_alphabet():
    """
    Imprime el alfabeto en mayúsculas en una sola línea, en orden decreciente.
    """
    os.system("cls")
    return print(string.ascii_uppercase[::-1])


def main():
    if len(sys.argv) == 1:
        print_reverse_alphabet()

    else:
        print("Uso: python print_reverse_alphabet.py")


if __name__ == "__main__":
    main()