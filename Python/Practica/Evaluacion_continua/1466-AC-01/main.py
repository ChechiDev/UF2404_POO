import sys
import os

def validation(txt):
    """
    Función recursiva que valida la entrada del usuario.
    Arg: txt (str): Mensaje input()

    Return: int: Valor numérico introducido por el usuario, entre 1 y 5.
    """
    while True:
        valor = input(txt).strip()

        if not (valor.isdigit() and len(valor) == 1):
            print("El valor introducido es inválido. Debe ser un solo dígito numérico entre 1 y 5.")
            input("Presiona Enter para continuar...")
            os.system("cls")
            continue

        valor = int(valor)
        if 1 <= valor <= 5:
            return valor

        else:
            print("El valor debe estar entre 1 y 5.")
            input("Presiona Enter para continuar...")
            os.system("cls")
            continue


def rectangle(x=None, y=None):
    """"
    Función que dibuja un rectángulo con las siguientes características:
    Arg1 = x: Base del rectángulo => int
    Arg2 = y: Altura del rectángulo => int

    Return: Lista 2D del rectángulo.
    matrix = [
        ["o", "-", "-", "-", "o"],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", " ", "|"],
        ["o", "-", "-", "-", "o"]
    ]
    """
    while x is None or y is None:
        os.system("cls")

        if x is None:
            x = validation("Introduce la base del rectángulo (1-5): ")
            os.system("cls")

        if y is None:
            y = validation("Introduce la altura del rectángulo (1-5): ")
            os.system("cls")


    # Creamos la lista 2D del rectángulo:
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            if (i == 0 and j == 0) or (i == 0 and j == x - 1) or (i == y - 1 and j == 0) or (i == y - 1 and j == x - 1):
                row.append("o")

            elif i == 0 or i == y - 1:
                row.append("-")

            elif j == 0 or j == x - 1:
                row.append("|")

            else:
                row.append(" ")

        matrix.append(row)

    # Mostramos contenido de la lista 2D:
    for row in matrix:
        print(" ".join(row))


def main():
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            rectangle(x, y)

        except ValueError:
            print("Los argumentos deben ser números enteros")

    else:
        print("Uso: python desafio.py <ancho> <alto>")
        

if __name__ == "__main__":
    rectangle() # Los args se piden por input()
    main()