import sys
import os

"""
Escribe un programa que ordene un array de int en orden ascendente.
El prototipo del main deberá ser el siguiente:

def main():

El prototipo de la función deberá ser el siguiente:

def sort_tab(arr);

"""
def sort_tab(arr):
    """
    Ordena un array de enteros en orden ascendente.
    Return:
        list: Lista de enteros ordenada.
    """
    os.system("cls")
    return sorted(arr)


def main():
    if len(sys.argv) == 2:

        try:
            # Comprobamos con un parámetro de compresión que lo que se introduce son enteros: Ej: 3,2,1
            arr = [int(x) for x in sys.argv[1].split(",")]
            print(sort_tab(arr))

        except ValueError:
            print("Error: El argumento debe ser una lista de enteros.")
            return

    else:
        print("Uso: python sort_tab.py <list>")


if __name__ == "__main__":
    main()