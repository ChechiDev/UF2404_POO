import sys
import os

"""
Escribe un programa ponga cada letra en mayúscula
La función deberá devolver un nuevo string y se imprimirá por pantalla
El prototipo del main deberá ser el siguiente:

def main():
		string = str(sys.argv[1])

El prototipo de la función deberá ser el siguiente:

def str_up_case(string):

Debes incluir el módulo sys:
import sys
"""

def str_up_case(x):
    """
    Devuelve un nuevo string con las letras en mayúscula.
    """
    os.system("cls")
    return x.upper()


def main():
    if len(sys.argv) == 2:
        x = sys.argv[1]
        print(str_up_case(x))

    else:
        print("Uso: python str_up_case.py <texto>")


if __name__ == "__main__":
    main()