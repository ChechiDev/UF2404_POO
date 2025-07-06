import sys
import os
import string

"""
Escribe un programa que tome un string y lo muestre, moviendo cada letra 1 posición en el alfabeto.
"z" será "a" y "Z" será "A".
Las cajas no se verán afectadas.
La string de salida estará seguida de una nueva línea.
Si el número de argumentos no es 1, simplemente se mostrará una nueva línea.
Ejemplos:
$>python mov_alpha.py “abc”
bcd

$>python mov_alpha.py “Les stagiaires du staff ne sentent pas toujours tres bon.” | cat -e
Mft tubhjbjsft ev tubgg of tfoufou qbt upvkpvst usft cpo.$

$>python mov_alpha.py “AkjhZ zLKIJz , 23y “ | cat -e
BlkiA aMLJKa , 23z $

$>python mov_alpha.py | cat -e
$
$>

$>python mov_alpha.py “” | cat -e
$
$>
"""

def get_next_char(char):
    """
    Devuelve la siguiente letra en el alfabeto.
    Cuando llega la final del alfabeto
    Si no es letra devuelve le mismo carácter
    """
    alph_low = string.ascii_lowercase
    alph_up = string.ascii_uppercase

    if char in alph_low:
        # Convertimos carácter a int
        idx = alph_low.index(char)
        # Calculamos el modulo, para el índice
        return alph_low[(idx + 1) % 26]

    # Lógica para las mayúsculas
    elif char in alph_up:
        idx = alph_up.index(char)
        return alph_up[(idx + 1) % 26]

    else:
        return char


def mov_alpha(text):
    """
    Devuelve un nuevo string donde cada letra se desplaza una posición en el alfabeto.
    La función respeta mayúsculas y minúsculas.
    """
    os.system("cls")
    res = ""

    for i in text:
        res += get_next_char(i)

    return res


def main():
    if len(sys.argv) == 2:
        text = sys.argv[1]
        print(mov_alpha(text))

    else:
        print()


if __name__ == "__main__":
    main()