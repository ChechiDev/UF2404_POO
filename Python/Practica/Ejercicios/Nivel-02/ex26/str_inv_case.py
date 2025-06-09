import sys
import os


"""
Escribe un programa que tome un string y cambie las letras minúsculas por mayúsculas y vicerversa.
El resto de caracteres no se verán afectados.
La string de salida estará seguida de una nueva línea.
Si el número de argumentos no es 1, simplemente se mostrará una nueva línea.
Ejemplos:
$>python str_inv_case “L'eSPrit nE peUt plUs pRogResSer s'Il staGne et sI peRsIsTent VAnIte et auto-justification.” | cat -e
l'EspRIT Ne PEuT PLuS PrOGrESsER S'iL STAgNE ET Si PErSiStENT vaNiTE ET AUTO-JUSTIFICATION.$

$>python str_inv_case “S'enTOuRer dE sECreT eSt uN sIGnE De mAnQuE De coNNaiSSanCe.  ” | cat -es
'ENtoUrER De SecREt EsT Un SigNe dE MaNqUe dE COnnAIssANcE.  $

$>python str_inv_case “3:21 Ba  tOut  moUn ki Ka di KE m'en Ka fe fot” | cat -e
3:21 bA  ToUT  MOuN KI kA DI ke M'EN kA FE FOT$

$>python str_inv_case | cat -e
$
"""

def str_inv_case(text):
    """
    Invierte de mayus a minus y viceversa cada letra en el string dado por arg.
    Los caracteres que no son letras permanecen sin cambios.
    """
    res = ""

    for i in text:
        if i.islower():
            res += i.upper()

        elif i.isupper():
            res += i.lower()

        else:
            res += i

    return res


def main():
    if len(sys.argv) == 2:
        text = sys.argv[1]
        print(str_inv_case(text))

    else:
        print()


if __name__ == "__main__":
    main()