import sys
import os

"""
# Caso Práctico -  Listas

### **Organizador de Biblioteca Personal**

Escribe un programa que tendrá una función llamada `increase_library` que recibirá un argumento: `new_book`

Dentro de la función `increase_library` se debe leer un listado de títulos de libros que el usuario ya ha leído. Esta lista se encuentra almacenada en un archivo de texto `books.txt`

[books.txt](attachment:69849629-b9ac-4615-98c4-369205d6582b:books.txt)

- Para leer el archivo `books.txt` utiliza la función por defecto `open()`
- Convierte el archivo que acabas de leer a una lista utilizando la siguiente sentencia:
`books = local_file.read().splitlines()`
- Termina la operación de lectura del archivo con la función `local_file.close()`

Dentro de la función, se debe añadir al final de la lista de libros el nuevo libro `(new_book)` especificado por el usuario.

La función debe devolver la lista completa de libros con el nuevo libro añadido.

El usuario debe mostrar por pantalla la lista completa de libros.

Adicionalmente, debe implementarse una nueva función llamada `first_book_read` que imprimirá por pantalla el primer libro que el usuario ha leído y ha añadido a la lista de libros.
Esta función recibirá como argumento la lista de libros y devolverá el primer libro de la lista.

El usuario debe mostrar por pantalla el primer libro de la lista.

### Resultado esperado

La biblioteca de libros leídos es:

`['Don Quijote de la Mancha', 'Orgullo y Prejuicio', 'Crimen y Castigo', 'Moby Dick', 'La Ilíada', 'El Gran Gatsby', 'Cien Años de Soledad', '1984', 'La Divina Comedia', 'Guerra y Paz', 'Las Aventuras de Huckleberry Finn']`

`El primer libro que he leído es: "Don Quijote de la Mancha"`
"""

# Creamos una variable global que contenga la ruta del archivo, con la data
data_src = r".\data\books.txt"

def load_book_data():
    """
    Función recursiva que carga los datos de los libros.
    Return:
        List: Lista con los libros existentes cargados.
    """

    # Cargamos la lista de libros existente en el archivo books.txt:
    with open(data_src, "r", encoding="UTF-8") as f:
        books = f.read().splitlines()
        f.close()

    return books


def increase_library(books, new_book):
    """
    Añade un nuevo libro a la lista de libros y lo guarda en el archivo de texto.
    Return:
        List: Lista actualizada con los libros
    """

    # Agregamos el nuevo libro a la lista y retornamos lista actualizada:
    books.append(new_book)

    # Agregamos el nuevo libro al archivo .txt con la data
    with open(data_src, "a", encoding="UTF-8") as f:
        f.write(f"\n{new_book}")
        f.close()

    return books


def first_book_read(books):
    """
    Función recursiva para mostrar el último libro leído
    Return:
        str: El nombre del primer libro leído
    """

    if books:
        return books[0]

    else:
        return None


def main():
    os.system("cls")

    # Cargamos el listado de libros:
    books = load_book_data()

    if len(sys.argv) == 1:
        new_book = input("Introduce el nombre del nuevo libro: ")

    # Si se introduce por terminal, recogemos:
    else:
        new_book = sys.argv[1]

    # Agregramos el nuevo libro a la lista existente
    books = increase_library(books, new_book)

    os.system("cls")
    # Mostramos el listado de libros:
    print("Listado de libros leídos: \n")

    for idx, book in enumerate(books, start=1):
        print(f"{idx}. {book}")

    print()

    # Agregamos la lógica para mostrar el primer y último libro leído:
    first_book = first_book_read(books)
    if first_book:
        print(f"El primer libro leído es: {first_book}")

    print()


if __name__=="__main__":
    main()