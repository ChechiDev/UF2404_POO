import sys
import os

"""
Escribe un programa que tome 3 argumentos, el primer argumento es un string en el cual se reemplazará la letra 2º argumento por la del 3er argumento.
Si el número de argumentos no es 3, simplemente se mostrará una nueva línea.
Si el 2º argumento no contiene ninguna letra del primer argumento (string) el programa simplemente escribirá el string seguido de una nueva línea.
Ejemplos:
$>python search_replace “Papache est un sabre” “a” “o”
Popoche est un sobre

$>python search_replace “zaz” “art” “zul” | cat -e
$

$>python search_replace “zaz” “r” “u” | cat -e
zaz$

$>python search_replace “jacob” “a” “b” “c” “e” | cat -e
$

$>python search_replace “ZoZ eT Dovid oiME le METol.” “o” “a” | cat -e
ZaZ eT David aiME le METal.$

$>python search_replace “wNcOre Un ExEmPle Pas Facilw a Ecrirw “ “w” “e” | cat -e
eNcOre Un ExEmPle Pas Facile a Ecrire $
"""


def search_replace(x, y, z):
    """
    Reemplaza todas las apariciones del carácter 'y' por el carácter 'z' en la cadena 'x'.

    Args:
        x (str): Cadena de texto original.
        y (str): Carácter a buscar y reemplazar.
        z (str): Carácter por el que se reemplaza.

    Returns:
        str: Nueva cadena con los reemplazos realizados.
    """

    os.system("cls")
    res = ""

    for i in x:
        if i == y:
            res += z

        else:
            res += i

    return res


def main():
    if len(sys.argv) == 4:
        x = sys.argv[1]
        y = sys.argv[2]
        z = sys.argv[3]
        print(search_replace(x, y, z))

    else:
        print()


if __name__ == "__main__":
    main()