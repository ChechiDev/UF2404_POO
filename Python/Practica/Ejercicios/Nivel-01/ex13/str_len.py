import sys


"""
Escribe un programa que cuente el número de caracteres de un string y que devuelva el número encontrado.
El prototipo del main deberá ser el siguiente:
def main():
		string = sys.argv[1]
        ​
El prototipo de la función deberá ser el siguiente:
def str_len(string):

Debes incluir el módulo sys:
import sys

Debes asegurar de que la función main() solo se ejecuta cuando este archivo se ejecuta directamente desde la línea de comandos
if __name__ == "__main__":
    main()
"""

def str_len(s):
    """
    Muestra la longitud de una cadena de texto por argumento.
    Arg1: str : Cadena de texto
    """
    return print(f"La longitud de la cadena es: {len(s)}")

def main():
    if len(sys.argv) == 2:
        try:
            s = str(sys.argv[1])
            str_len(s)

        except ValueError:
            print("Error: El argumento debe ser una cadena de texto.")
            return

    else:
        print("Uso: python str_len.py <cadena>")
        return

if __name__ == "__main__":
    main()