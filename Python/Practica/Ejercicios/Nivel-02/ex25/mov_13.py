import sys
import os
import string

"""
Escribe un programa que tome un string y lo muestre, moviendo cada letra 13 posiciones en el alfabeto.
"z" será "m" y "Z" será "M".
Las cajas no se verán afectadas.
La string de salida estará seguida de una nueva línea.
Si el número de argumentos no es 1, simplemente se mostrará una nueva línea.
Ejemplos:
$>python mov_13 “abc”
nop

$>python mov_13 “My horse is Amazing.” | cat -e
Zl ubefr vf Nznmvat.$

$>python mov_13 “AkjhZ zLKIJz , 23y “ | cat -e
NxwuM mYXVWm , 23l $

$>python mov_13 | cat -e
$
$>

$>python mov_13 “” | cat -e
$
$>
"""

def get_next_char(char):
    """
    Devuelve la siguiente letra en el alfabeto desplazando 13 posiciones.
    Cuando llega la final del alfabeto
    Si no es letra devuelve le mismo carácter
    """
    alph_low = string.ascii_lowercase
    alph_up = string.ascii_uppercase

    if char in alph_low:
        # Convertimos carácter a int
        idx = alph_low.index(char)
        # Calculamos el modulo, para el índice
        return alph_low[(idx + 13) % 26]

    # Lógica para las mayúsculas
    elif char in alph_up:
        idx = alph_up.index(char)
        return alph_up[(idx + 13) % 26]

    else:
        return char


def mov_13(text):
    """
    Devuelve un nuevo string donde cada letra se desplaza 13 posiciones en el alfabeto.
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
        print(mov_13(text))

    else:
        print()


if __name__ == "__main__":
    main()