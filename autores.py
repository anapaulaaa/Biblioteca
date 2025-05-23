class Autor:
    libros = list()
    def __init__(self):
        pass
    def AgregarAutor(self, nombre, apellido, nacionalidad, codigo):
        self.nombres = nombre
        self.apellidos = apellido
        self.nacionalidad = nacionalidad
        self.codigo = codigo
        self.libros = Autor.libros

    def AgregarLibro(self, libro):
        self.libros.append(libro)
    
    def VerLibrosPorAutor(self):
        for i in range(len(self.libros)):
            print(f"{self.libros[i]}")
