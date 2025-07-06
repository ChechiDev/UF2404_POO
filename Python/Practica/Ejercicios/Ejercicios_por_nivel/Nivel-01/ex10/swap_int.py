import sys
import os

"""
Escribe un programa que intercambie el contenido y las direcciones de memoria de dos enteros
El prototipo del main deberá ser el siguiente:
def main():

El prototipo de la función deberá ser el siguiente:
def swap_int(a, b):

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""

def swap_int(a, b):
    """
    Intercambia el contenido y las direcciones de memoria (id) de dos enteros.
    """
    os.system("cls")

    a = id(b)
    b = id(a)

    return print(a), print(b)


def main():
    if len(sys.argv) == 3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            swap_int(a, b)

        except ValueError:
            print("Error: Los argumentos deben ser enteros.")
            return

    else:
        print("Uso: python swap_int.py <integer1> <integer2>")
        return


if __name__ == "__main__":
    main()