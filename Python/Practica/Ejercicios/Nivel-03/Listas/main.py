import sys

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

def first_book_read(b):
    pass


def increase_library(new_book):
    local_file = r"./DATA/books.txt"
    
    b = open(local_file).read().splitlines()
    b.append(new_book)

    print(b)
    return


def main():
    if len(sys.argv) == 1:
        new_book = input("Introduce el nombre del nuevo libro: ")    
        increase_library(new_book)


if __name__=="__main__":
    main()