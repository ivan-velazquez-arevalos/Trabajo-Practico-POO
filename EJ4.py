# Ejercicio 4. Libro de una biblioteca
# Una biblioteca lleva el registro de sus libros.
# Modelá una clase Libro con su título, autor y un estado que indique si está disponible o prestado.
# La clase debe poder mostrar la ficha del libro indicando su situación actual.

class Libro:
    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya se encuentra prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto y está disponible.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: '{self.titulo}' | Autor: {self.autor} | Estado: {estado}"

if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", disponible=True)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", disponible=False)

    print("Estado Inicial de los Libros:")
    print(libro1)
    print(libro2)

    print("\nPréstamo y Devolución de los Libros:")
    libro1.prestar()
    libro2.devolver()

    print("\nEstado Final de los Libros:")
    print(libro1)
    print(libro2)