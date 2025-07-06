import sys
import os

"""
Escribe un programa que invierta un array de int (el primer elemento va el último, etc)
"""

def inv_tab(x: list):
    """
    Invierte una lista de elementos int()
    """
    os.system("cls")
    return print(x[::-1])


def main():
    if len(sys.argv) == 2:

        try:
            x = list(sys.argv[1])

            inv_tab(x)

        except ValueError:
            print("Se debe introducir una lista")

    else:
        print("Uso. python inv_tab.py <list_num>")
        return


if __name__ == "__main__":
    main()