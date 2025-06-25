import sys

def rectangle(x, y):
    """
    Dibuja un rectángula de X columnas y Y filas:
    Arg1: X (int)
    Arg2: Y (int)
    Return: No retorna nada, solo imprime el rectángulo.
    """

    if (x <= 0 or y == 0):
        return
    
    # Construimos rect:
    for row in range(y):
        if (row == 0 or row == y -1):
            if (x == 1):
                print("o")
            
            else:
                print("o" + "-" * (x - 2) + "o")
            
        else:
            if (x == 1):
                print("|")

            else:
                print("|" + " " * (x - 2) + "|")



def main():
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            rectangle(x, y)
        
        except ValueError:
            print("Los argumentos deben ser int()")

    else:
        print("Uso: python main.py <ancho> <alto>")


if __name__ == "__main__":
    main()