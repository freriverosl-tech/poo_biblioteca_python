class Libro:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    # Métodos accesadores
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_paginas(self):
        return self.__paginas

    # Métodos mutadores
    def set_titulo(self, titulo):
        self.__titulo = titulo
    def set_autor(self, autor):
        self.__autor = autor
    def set_paginas(self, paginas):
        if paginas > 0:
            self.__paginas = paginas
        else:
            print("El número de páginas debe ser mayor que 0")


class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print("-", libro.get_titulo(), "Autor:", libro.get_autor(), "Páginas:", libro.get_paginas())


class Estante:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def mostrar_libros(self):
        print("Libros en el estante:")
        for libro in self.libros:
            print("-", libro.get_titulo())


# Crear objetos Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("1984", "George Orwell", 328)
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
libro4 = Libro("Fahrenheit 451", "Ray Bradbury", 194)


# Modificar un dato usando setter
libro2.set_paginas(350)

# Crear objeto Biblioteca y agregar libros
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)


# Crear objeto Estante y agregar libros
estante = Estante()
estante.agregar_libro(libro1)
estante.agregar_libro(libro2)
estante.agregar_libro(libro3)
estante.agregar_libro(libro4)


# Mostrar libros en ambos
biblioteca.mostrar_libros()
print()
estante.mostrar_libros()
