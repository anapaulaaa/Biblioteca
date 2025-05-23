from autores import Autor
from libros import Libro
import os


def menu():
    autores = list()
    on = True
    
    while on:
        os.system("cls")
        print("Menu")
        print("1. Agregar Autor")
        print("2. Ver listado de autores")
        print("3. Agregar Libro a Autor")
        print("4. Ver Libros por autor")
        print("0. Salir")
        print("-" * 30)
        opc = int(input("Ingrese una opcion: "))
        
        if opc == 1:
            codigo = int(input("Ingrese codigo del Autor: "))
            apellidos = input("Ingrese apellidos del Autor: ")
            nombres = input("Ingrese nombres del Autor: ")
            nacionalidad = input("Ingrese nacionalidad del Autor: ")
            autor1 = Autor()
            autor1.AgregarAutor(nombres, apellidos, nacionalidad, codigo)
            autores.append(autor1)
        elif opc == 2:
            for MisAutores in autores:
                print(f"{MisAutores.codigo}\t{MisAutores.apellidos}\t{MisAutores.nombres}\t{MisAutores.nacionalidad}")
            input()
        elif opc == 3:
            codigo = int(input("Ingrese el codigo del Autor: "))
            for i in range(len(autores)):
                if autores[i].codigo == codigo:
                    titulo = input("Ingrese titulo del Libro: ")
                    tipo = input("Ingese tipo de Libro: ")
                    libro1 = Libro(titulo, tipo)
                    autores[i].AgregarLibro(libro1)
                else:
                    continue
        elif opc == 4:
            for i in range(len(autores)):
                print(f"{autores[i].VerLibrosPorAutor()}")
            input()
        elif opc == 0:
            on = False
        else:
            print("Ingrese una opcion valida!!")
            
menu()