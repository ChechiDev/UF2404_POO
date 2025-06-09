import sys
import os

"""
Escribe un programa que muestre, “N” o “P” en función del signo del entero que se haya usado como parámetro. Si n es negativo muestra “N”. Si n es positivo o nulo muestra “P”.
El prototipo del main deberá ser el siguiente:
def main():
    n = int(sys.argv[1])

El prototipo de la función deberá ser el siguiente:
def is_negative(n):

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""

def is_negative(n):
    os.system("cls")
    return print("N") if n < 0 else print("P")


def main():
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
            is_negative(n)

        except ValueError:
            print("Por favor, introduce un número entero como argumento.")

    else:
        print("Uso: python is_negativ.py <número entero>")


if __name__ == "__main__":
    main()