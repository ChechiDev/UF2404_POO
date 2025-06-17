import os
import re
from pprint import pprint

"""
### **Gestor de Experiencia Laboral y Creación de CV**

Escribe un programa que tendrá una función llamada `add_skills` que recibe dos argumentos: `work_profile` y `new_skill`

- `work_profile` será un diccionario que contiene información personal del usuario: `name`, `surname`, `age`, `city`, `skills`. Este último valor debe corresponderse con una lista que contendrá las experiencias laborales.
- `new_skill` será una variable tipo `string` que indica el nuevo puesto de trabajo.

Dentro de la función `add_skills`, añade `new_skill` a la lista de experiencias en `work_profile` y retorna el `work_profile` como resultado de la función.

Crea otra función llamada `generate_min_cv` que tome `work_profile`como argumento e imprima por pantalla un resumen del CV (con el formato especificado en las secciones siguientes), incluyendo la información personal y las experiencias laborales.

Fuera de las funciones añade una nueva experiencia laboral a tu perfil utilizando la función `add_skills` y llama a la función `generate_min_cv` tomando como argumento el resultado de la función `add_skills` para visualizar tu CV.
"""

class Utils:
    # Validaciones regex:
    @staticmethod
    def is_empty(x: str) -> bool:
        """
        Devuelve True si el valor está vacío o solo contiene espacios
        """
        return bool(re.fullmatch(r"\s*", x))

    @staticmethod
    def starts_with_space(x: str) -> bool:
        """
        Comprueba si el nombre introducido empieza por uno o varios espacios
        """
        return bool(re.search(r"^\s", x))

    @staticmethod
    def no_accent(x: str) -> bool:
        """
        Comprueba si el nombre introducido contiene acentos
        """
        return bool(re.search(r"[áéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛ]", x))

    @staticmethod
    def is_digit(x: str) -> bool:
        """
        Comprueba si el nombre introducido contiene números o carácteres especiales:
        """
        return bool(re.search(r"[^a-zA-Z\s]", x))

    @staticmethod
    def is_valid_lenght(x: str) -> bool:
        """
        Comprueba si el nombre introducido contiene al menos 3 carácteres hasta 30:
        """
        return bool(re.fullmatch(r".{3,30}", x.strip()))


class WorkprofileValidation:

    @staticmethod
    def valid_name() -> str:
        """
        Método de validación para el nombre del user:
        Arg: str <name>

        Return: str <verified name>
        """
        while True:
            os.system("cls")

            # Solicitamos la información al user:
            name = input("Introduce tu nombre: ")

            # Validamos que el nombre no esté vacío:
            if Utils.is_empty(name):
                print("El nombre no puede estar vacío.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el nombre no empiece con un espacio:
            elif Utils.starts_with_space(name):
                print(f"El nombre '{name}' no puede empezar con un espacio.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el nombre no tenga accentos:
            elif Utils.no_accent(name):
                print(f"El nombre '{name}' no puede contener acentos.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el nombre no sea alfanumérico:
            elif Utils.is_digit(name):
                print(f"El nombre '{name}' no puede contener ni números ni carácteres especiales.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el nombre cómo mínimo tenga 3 carácteres y un max de 30:
            elif not Utils.is_valid_lenght(name):
                print(f"El nombre '{name}' debe tener cómo mínimo de 3 a 30 carácteres válidos.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            else:
                return name

    @staticmethod
    def valid_surname() -> str:
        """
        Método de validación para apellido del user:
        Arg: str <surname>

        Return: str <verified surname>
        """
        while True:
            os.system("cls")

            # Solicitamos la información al user:
            surname = input("Introduce tu apellido: ")

            # Validamos que el apellido no esté vacío:
            if Utils.is_empty(surname):
                print("El apellido no puede estar vacío.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el apellido no empiece con un espacio:
            elif Utils.starts_with_space(surname):
                print(f"El apellido '{surname}' no puede empezar con un espacio.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el apellido no tenga accentos:
            elif Utils.no_accent(surname):
                print(f"El apellido '{surname}' no puede contener acentos.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el apellido no sea alfanumérico:
            elif Utils.is_digit(surname):
                print(f"El apellido '{surname}' no puede contener ni números ni carácteres especiales.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            # Validamos que el apellido cómo mínimo tenga 3 carácteres y un max de 30:
            elif not Utils.is_valid_lenght(surname):
                print(f"El apellido '{surname}' debe tener cómo mínimo de 3 a 30 carácteres válidos.\nInténtalo de nuevo...")
                input("\nPresione Enter para continuar...")
                continue

            else:
                return surname


class WorkprofileEntities:
    def __init__(self):
        # Validamos todos los atributos antes de generar el dict:
        self.name = WorkprofileValidation.valid_name()
        self.surname = WorkprofileValidation.valid_surname()

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname
        }


def main():
    os.system("cls")

    # Instancia:
    wprof = WorkprofileEntities()

    # Inprimimos la info en forma de dict:
    print(wprof.to_dict())


if __name__ == "__main__":
    main()
