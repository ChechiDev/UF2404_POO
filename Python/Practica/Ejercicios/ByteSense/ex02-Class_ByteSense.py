import os

"""
Actualización del ejercicio ByteSense de encriptado, con clase, métodos y utils
"""

class ByteEncryptor:
    """
    Clase principal para encryptación de texto.
    Return:
        Hex: Text encrypted
    """
    def __init__(self, txt, slicing):
        self.txt = txt
        self.slc = slicing

    def encrypt(self):
        """
        Función que devuelve el texto introducido, encriptado, de forma Hexadecimal
        Return: Hex
        """
        self.byte_txt = byte_utils.to_bytes(self.txt)
        self.byte_even = byte_utils.extract_even_bytes_and_concat(self.byte_txt)
        self.bytearr = byte_utils.str_to_bytearray(self.byte_even)
        self.xor = byte_utils.xor_method(self.bytearr, self.slc)
        self.hex = byte_utils.to_hex(self.xor)

        return self.hex

    def decrypt(self, hex=None):
        """
        Función que devuelve el texto introducido, desencriptado
        Return: str
        """
        # Preguntamos al user si quiere desencriptar el hex, en este caso cogemos el hex previamente introducido, sinó input()
        if hex is None:
            hex = self.hex

        self.hex = hex
        self.hex_to_str = byte_utils.from_hex(self.hex)
        self.xor = byte_utils.xor_method(self.hex_to_str, self.slc)
        self.byte_txt = byte_utils.restore_original_bytes(self.xor)

        return self.byte_txt


class byte_utils:
    """
    Clase recursiva, que contiene los métodos de transformación y cálculo.
    """

    @staticmethod
    def to_bytes(txt):
        return txt.encode("UTF-8")

    @staticmethod
    def extract_even_bytes_and_concat(txt):
        return txt + txt[::2]

    @staticmethod
    def restore_original_bytes(txt):
        # Guardamos la longitud del texto original antes de concatenar.
        # Duplicamos el texto y dividimos // 3 para extraer el resto
        # Porque doy por hecho que el texto concatenado con los pares es un 1.5 más grande que el texto original
        len_text = (len(txt) * 2) // 3
        return txt[ : len_text].decode("UTF-8")

    @staticmethod
    def str_to_bytearray(txt):
        return bytearray(txt)

    @staticmethod
    def xor_method(txt, slicing):
        for i in range(len(txt)):
            txt[i] ^= (i + slicing) % 256

        return txt

    @staticmethod
    def to_hex(txt):
        """
        Convierte un str a hexadecimal
        """
        return txt.hex()

    @staticmethod
    def from_hex(txt):
        """
        Convierte un texto hexadecimal a bytearray
        """
        return bytearray(bytes.fromhex(txt))
    

def main():
    os.system("cls")

    # Guardamos las opciones:
    opts = ["Encriptar", "Desencriptar", "Salir"]

    # Guardamos la selección del user:
    print("# ======== PRUEBA INTERACTIVA ======== #\n")
    for idx, opts in enumerate(opts):
        print(f"{idx + 1}. {opts}")

    select = input("\nSeleccione una opción: ")

    # Vinculamos las opciones:
    if select == "1":
        os.system("cls")
        print("# ======== PRUEBA INTERACTIVA ======== #\n")
        txt_input = input("Introduzca un texto a encriptar: ")
        slicing_input = input("Introduzca el desplazamiento (por defecto 1): ")
        slicing = int(slicing_input) if slicing_input else 1

        # Creamos la instancia a la clase Master:
        byte_encrypt = ByteEncryptor(txt_input, slicing)
        encrypt_res = byte_encrypt.encrypt()

        # Mostramos resultado:
        os.system("cls")
        print("# ======== PRUEBA INTERACTIVA ======== #\n")
        print(f"Texto encriptado (hex): {encrypt_res}")
        print()
        
        opt = input("Desea volver a desencriptar el texto? (S/N): ").strip().lower()
        
        if opt == "s":
            os.system("cls")
            print("# ======== PRUEBA INTERACTIVA ======== #\n")
            decrypt_res = byte_encrypt.decrypt(encrypt_res)
            print(f"Texto desencriptado: {decrypt_res}")
            print()
            input("Presione Esc para salir...")
            main()
        
        elif opt == "n":
            main()

        else:
            print("Opción inválida...")
            main()


    elif select == "2":
        os.system("cls")
        print("# ======== PRUEBA INTERACTIVA ======== #\n")
        hex_input = input("Introduzca un texto a desencriptar: ")
        slicing_input = input("Introduzca el desplazamiento (por defecto 1): ")
        slicing = int(slicing_input) if slicing_input else 1

        # Creamos la instancia con ByteEncryptor:
        byte_decrypt = ByteEncryptor(hex_input, slicing)
        decrypt_res = byte_decrypt.decrypt(hex_input)

        os.system("cls")
        print("# ======== PRUEBA INTERACTIVA ======== #\n")
        print(f"Texto desencriptado (str): {decrypt_res}\n")


    elif select == "3":
        os.system("cls")
        print("# ======== PRUEBA INTERACTIVA ======== #\n")
        print("Gracias por si visita!\n")
        return


    else:
        print("\nOpción inválida...")
        input("Presione Esc para salir...")
        main()

if __name__ == "__main__":
    main()