import sys
import os
import string

"""
Escribe un programa llamado repeat_case que tome un string y lo muestre repitiendo cada carácter alfabético tantas veces como su índice alfabético, seguido de una nueva de línea.
"a" será "a", "b" será "bb", "e" será "eeeee", etc...
Las cajas permanecerán sin cambios.
Si el número de argumentos no es 1, simplemente se mostrará una nueva línea.
Ejemplos:
$>python repeat_case.py  “abc”
abbccc

$>python repeat_case.py “Alex.” | cat -e
Alllllllllllleeeeexxxxxxxxxxxxxxxxxxxxxxxx.$

$>python repeat_case.py "abacadaba 83!" | cat -e
abbacccaddddabba 83!$

$>python repeat_case.py | cat -e
$
$>

$>python repeat_case.py | cat -e
$
$>
"""

def get_len(char):
    alph = string.ascii_lowercase

    # Comprobamos si la letra está dentro del alfabeto sinó retornamos 1
    if char.lower() in alph:
        return alph.index(char.lower()) + 1

    else:
        return 1


def repeat_case(text):
    os.system("cls")

    # Guardamos resultado:
    res = ""

    for i in text:
        # Comprobamos que el carácter sea una letra dentro del alfabeto, sinó 1
        if i.isalpha():
            res += i * get_len(i)

        else:
            res += i

    return res


def main():
    if len(sys.argv) == 2:
        text = sys.argv[1]
        print(repeat_case(text))

    else:
        print("Uso: python repeat_case.py <texto>")


if __name__ == "__main__":
    main()