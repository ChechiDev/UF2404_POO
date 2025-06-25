import os
from main import rectangle, validation

def bonus_track(x=None, y=None, z=None):
    """
    Función principal que ejecuta la función correspondiente según el tipo de rectángulo elegido.
    Arg1 = x: Base del rectángulo => int
    Arg2 = x: Altura del rectángulo => int
    Arg3 = z: Tipo de rectángulo => str

    Return: Lista 2D del rectángulo según el tipo elegido, sin espacios.
    """
    os.system("cls")

    x = validation("Introduce la base del rectángulo (1-5): ")
    os.system("cls")
    y = validation("Introduce la altura del rectángulo (1-5): ")
    os.system("cls")

    # Validamos que se introduce bien el tipo de rectángulo:
    while True:
        z = input("Introduce el tipo de rectángulo (A, B, C): ").lower().strip()
        os.system("cls")

        if z in ["a", "b", "c"]:
            break

        else:
            print("Opción inválida. Debe ser A, B o C.")

    if z == "a":
        rectangle_a(x, y)

    elif z == "b":
        rectangle_b(x, y)

    elif z == "c":
        rectangle_c(x, y)


def rectangle_a(x, y, z=None):
    """
    Función recursiva que dibuja un rectángulo de forma recursiva.
    Arg1 = x: Base del rectángulo => int
    Arg2 = y: Altura del rectángulo => int
    Arg3 = z: Tipo de rectángulo => str

    return: Lista 2D del rectángulo, sin espacios.
    matrix = [
        ["o", "-", "-", "o"],
        ["|", " ", " ", "|"],
        ["o", "-", "-", "o"]
    ]
    """
    rectangle(x, y)


def rectangle_b(x, y, z=None):
    """
    Función que dibuja un rectángulo con las siguientes características:
    Arg1 = x: Base del rectángulo => int
    Arg2 = y: Altura del rectángulo => int
    Arg3 = z: Tipo de rectángulo => str

    Return: Lista 2D del rectángulo, sin espacios.
    matrix = [
        ["B", "/", "/", "/", "B"],
        ["/", " ", " ", " ", "/"],
        ["B", "/", "/", "/", "B"]
    ]
    """
    # Creamos la lista 2D del rectángulo:
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            if (i == 0 and j == 0) or (i == 0 and j == x - 1) or (i == y - 1 and j == 0) or (i == y - 1 and j == x - 1):
                row.append("B")

            elif i == 0 or i == y - 1:
                row.append("/")

            elif j == 0 or j == x - 1:
                row.append("/")

            else:
                row.append(" ")

        matrix.append(row)

    # Mostramos:
    for row in matrix:
        print("".join(row))


def rectangle_c(x, y, z=None):
    """
    Función que dibuja un rectángulo con las siguientes características:
    Arg1 = x: Base del rectángulo => int
    Arg2 = y: Altura del rectángulo => int
    Arg3 = z: Tipo de rectángulo => str

    Return: Lista 2D del rectángulo, sin espacios.
    matrix = [
        ["O", "x", "A", "x", "O"],
        ["x", "O", "B", "O", "x"],
        ["O", "x", "A", "x", "O"]
    """
    # Creamos el lista 2D del rectángulo
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            if i == 0 or i == y - 1:
                if j == 0 or j == x - 1:
                    row.append("O")

                elif j == 1 or j == x - 2:
                    row.append("x")

                elif j == x // 2:
                    row.append("A")

                else:
                    row.append(" ")


            # Matriz del centro:
            elif i == y // 2:
                if j == 0 or j == x - 1:
                    row.append("x")

                elif j == 1 or j == x - 2:
                    row.append("O")

                elif j == x // 2:
                    row.append("B")

                else:
                    row.append(" ")

            else:
                row.append(" ")

        matrix.append(row)

    for row in matrix:
        print("".join(row))


if __name__ == "__main__":
    bonus_track()