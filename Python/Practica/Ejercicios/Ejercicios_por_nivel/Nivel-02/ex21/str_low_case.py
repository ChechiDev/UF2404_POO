import sys
import os

"""
Crea un programa que ponga cada letra en minúsculas.
La función deberá devolver un nuevo string y se imprimirá por pantalla
El prototipo del main deberá ser el siguiente:

def main():
		string = str(sys.argv[1])


El prototipo de la función deberá ser el siguiente:

def str_low_case(string);

Debes incluir el módulo sys:
import sys
"""

def str_low_case(x):
    """
    Devuelve un nuevo string con las letras en minúscula.
    """
    os.system("cls")
    return x.lower()


def main():
    if len(sys.argv) == 2:
        x = sys.argv[1]
        print(str_low_case(x))

    else:
        print("Uso: python str_low_case.py <texto>")


if __name__ == "__main__":
    main()