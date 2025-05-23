class Autor:
    #Eliminar el atributo de clase
    #libro = list() 
    def __init__(self):
        pass
    def AgregarAutor(self, nombre, apellido, nacionalidad, codigo):
        self.nombres = nombre
        self.apellidos = apellido
        self.nacionalidad = nacionalidad
        self.codigo = codigo
        #agregar una variable de instancia, en este caso es similar a lo que habiamos hecho, solo que de esta forma esta lista de libros es propia del objeto
        self.libros = list() #Con esto eliminamos el error que teniamos al agregar los libros que se los agregaba a todos los autores

    #Agragar una funcion para añadir los libros pasados por la clase libros, a nuestra lista de libros
    def AgregarLibro(self, libro):
        self.libros.append(libro)
    
    def VerLibrosPorAutor(self):
        #Este metodo imprime los libros agregados al autor
        if not self.libros:
            #Imprime un mensaje si no hay libros agregados
            print(f"{self.apellidos} {self.nombres}")
            print("No tiene libros agregados")
        else:
            #Imprime los libros agregados del autor
            print(f"{self.apellidos} {self.nombres}")
            for book in range(len(self.libros)):
                print(f"{self.codigo} -> {self.libros[book]}")
