import sys
import os

"""
Escribe un programa que muestre, en orden creciente, todas las combinaciones posibles de tres dígitos distintos en orden creciente -sí, la repetición es voluntaria.
El prototipo del main deberá ser el siguiente:
def main():


El resultado es algo parecido a esto:
$>python print_comb.py
012, 013, 014, 015, 016, 017, 018, 019, 023, ..., 789
$>

987 no está porque 789 ya existe.
999 no está porque este número no contiene exclusivamente dígitos distintos.
El prototipo de la función deberá ser el siguiente:

def print_comb():

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""

def print_comb():
    """
    Imprime todas las combinaciones posibles de tres dígitos distintos, sin repetirse entre ellos, en orden creciente.
    """

    os.system("cls")
    comb = []
    n1 = 0
    n2 = 0
    n3 = 0

    for n1 in range(10):
        # comb.append(str(n1))

        for n2 in range(n1 + 1, 10):
            # if n2 not in comb:
                # comb.append(str(n1) + str(n2))

                for n3 in range(n2 + 1, 10):
                    # if n3 not in comb:
                        comb.append(str(n1) + str(n2) + str(n3))

    print(comb)


def main():
    print_comb()

if __name__ == "__main__":
    main()