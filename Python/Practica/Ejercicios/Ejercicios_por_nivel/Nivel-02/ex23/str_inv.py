import sys
import os

"""
Escribe un programa que tome un string y lo muestre el string invertido, seguido de una nueva línea.
Si el número de argumentos no es 1, simplemente se mostrará una nueva línea.
Ejemplos:
$>python str_inv.py “zaz” | cat -e
zaz$

$>python str_inv.py “dub0 a POIL” | cat -e
LIOP a 0bud$

$> python str_inv.py | cat -e
$
"""

def str_inv(s):
    os.system("cls")
    return s[::-1]


def main():
    if len(sys.argv) == 2:
        s = sys.argv[1]
        print(str_inv(s))

    else:
        print()


if __name__ == "__main__":
    main()