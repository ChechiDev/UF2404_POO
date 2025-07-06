import sys
import os

"""
Escribe un programa que muestre, todas las combinaciones posibles de dos números (XX XX) entre 0 y 99, en orden creciente.
El prototipo del main deberá ser el siguiente:
def main():


El resultado es algo parecido a esto:
$>python print_comb2.py
00 01, 00 02, 00 03, 00 04, 00 05, ..., 00 99, 01 02, ..., 97 99, 98 99
$>


El prototipo de la función deberá ser el siguiente:
def print_comb2():

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""

def print_comb2():
    """
    Imprime todas las combinaciones posibles de dos números (XX XX) entre 0 y 99, en orden creciente.
    """

    os.system("cls")

    result = []

    for n1 in range(0, 99):
        for n2 in range(n1 + 1, 100):
            if n1 < 10:
                n1_str = f"0{n1}"

            else:
                n1_str = str(n1)

            if n2 < 10:
                n2_str = f"0{n2}"

            else:
                n2_str = str(n2)

            result.append(f"{n1_str} {n2_str}")

    print(result)


def main():
    print_comb2()

if __name__ == "__main__":
    main()