from autores import Autor
from libros import Libro
import os


def menu():
    autores = list()
    on = True
    
    while on:
        #Impresion de las opciones de menu
        os.system("cls")
        print("Menu")
        print("1. Agregar Autor")
        print("2. Mostrar Autor")
        print("3. Agregar Libro")
        print("4. Mostrar Libros Por Autor")
        print("0. Salir")
        print("-" * 30)
        #Esperando la entrada del usuario
        opc = int(input("Ingrese una opcion: "))
        
        #verificando la opcion ingresada
        if opc == 1:
            #Agregar Autor
            os.system("cls")
            codigo = int(input("Ingrese codigo del Autor: "))
            apellidos = input("Ingrese apellidos del Autor: ")
            nombres = input("Ingrese nombres del Autor: ")
            nacionalidad = input("Ingrese nacionalidad del Autor: ")
            autor1 = Autor()
            autor1.AgregarAutor(nombres, apellidos, nacionalidad, codigo)
            autores.append(autor1)
        elif opc == 2:
            #Mostrar Autor
            os.system("cls")
            if not autores:
                print("No hay autores registrados") #Si no hay autores imprime
            else:
                #Imprime los autores agregados
                print("Codigo\t|Apellidos\t|Nombres\t|Nacionalidad")
                for MisAutores in autores:
                    print(f"{MisAutores.codigo}\t|{MisAutores.apellidos}\t\t|{MisAutores.nombres}\t\t|{MisAutores.nacionalidad}")
            input()
        elif opc == 3:
            #Agregar Libro
            os.system("cls")
            codigo = int(input("Ingrese el codigo del Autor: "))
            for i in range(len(autores)):
                #Verifica el codigo del autor y lo agrega al que corresponde
                if autores[i].codigo == codigo:
                    titulo = input("Ingrese titulo del Libro: ")
                    tipo = input("Ingese tipo de Libro: ")
                    libro1 = Libro(titulo, tipo)
                    autores[i].AgregarLibro(libro1)
                else: 
                    #Si el codigo no esta disponible 
                    print("Ingrese un codigo valido")
                    input()
        elif opc == 4:
            os.system("cls")
            if not autores:
                #Por si no hay autores registrados
                print("No hay autores")
            else:
                #Imprime los libros de cada autor
                for i in range(len(autores)):
                    autores[i].VerLibrosPorAutor()
            input()
        elif opc == 0:
            on = False
        else:
            print("Ingrese una opcion valida!!")

#Corriendo Funcion del menu            
menu()
