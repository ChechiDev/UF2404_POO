import sys

def bonus_track(x, y, z):
    """
    Dibuja un rectángulo donde X es la base y Y la altura.
    X = Int
    Y = Int
    Z = Str: tipo de patrón del rectángulo.
    """
    if (
        (x < 1 or y < 1) or 
        (z != "A" and z != "B" and z != "C")
        ):
        
        return print("Error!")
    
    for row in range(y):
        if z == "A":
            if row == 0 or row == (y - 1):
                if (x == 1):
                    print("o")
                
                else:
                    print("o" + "-" * (x - 2) + "o")
            
            else:
                if (x == 1):
                    print("|")

                else:
                    print("|" + " " * (x - 2) + "|")
    
    
        elif z == "B":
            if row == 0 or row == (y - 1):
                if (x == 1):
                    print("B")
                
                else:
                    print("B" + "/" * (x - 2) + "B")
            
            else:
                if (x == 1):
                    print("/")

                else:
                    print("/" + " " * (x - 2) + "/")
        
        # Caso C
        else:
            if(row == 0 or row == (y - 1)):
                if (x == 1):
                    print("0")

                elif (x == 2):
                    print("xx")

                elif (x == 3):
                    print("x0x")

                else:
                    print("xx")
    

def main():
    # En este cason es == 4, porque se piden 3 argumentos + la columna main.py
    if len(sys.argv) == 4:
        try:
            x = int(sys.argv[1]) 
            y = int(sys.argv[2])
            z = str(sys.argv[3])
            bonus_track(x, y, z)

        except ValueError:
            print("Los argumentos tienen que ser Int(1, 2) y Str(3)")

    else:
        print("Uso: python main.py <ancho> <alto> <tipo>")
        

if __name__ == "__main__":
    main()