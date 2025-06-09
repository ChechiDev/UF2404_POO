import sys
import os

"""
Escribe un programa que muestre, en una sola línea y en orden creciente, todos los dígitos.
El prototipo del main deberá ser el siguiente:
def main():

El prototipo de la función deberá ser el siguiente:
def print_numbers():

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""

def print_numbers():
    """
    Imprime los números del 1 al 10 en una sola línea.
    """
    os.system("cls")
    for i in range(1, 11):
        print(i, end = " ")


def main():
    if len(sys.argv) == 1:
        print_numbers()

    else:
        print("Uso: python print_numbers.py")


if __name__ == "__main__":
    main()