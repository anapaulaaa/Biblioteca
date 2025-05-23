class Libro:
    def __init__(self, titulo, tipo):
        self.__titulo = titulo
        self.__tipo = tipo

    @property
    def _titulo(self):
        return self.__titulo

    @_titulo.setter
    def _titulo(self, value):
        self.__titulo = value

    @property
    def _tipo(self):
        return self.__tipo

    @_tipo.setter
    def _tipo(self, value):
        self.__tipo = value

    def __str__(self):
        return f"{self.__titulo} {self.__tipo}"
