# -*- coding: utf-8 -*-

class Administrar:

    def __init__(self):   # Metodo constructor sin parametros
        pass

    def Menu(self):       # Super metodo Menu. este llama a otros metodos

        print("Bienvenido@ a la aplicacion.\n")
        print("Seleccione una Opcion del Menu: \n")

        print("1.- Agregar.")
        print("2.- Listar.")
        print("3.- Buscar.")
        print("4.- Eliminar.")
        print("5.- Salir.\n")

    def agregar(self):

        print("Ha seleccionado Agregar.")
        ## APERTURA DE UN ARCHIVO PARA AGREGAR ELEMENTOS
        Fichero = open("Login.csv",'a')   # Se abre el archivo Para escribir y
                                                    # Y se agrega el contenido q se le escriba
                                                    # al archivo Sin Borrar lo anterior ('a')
        Cuenta = raw_input("Introduce a que cuenta pertenece el login: ")
        Usuario = raw_input("Introduce el nombre de usuario: ")
        Password = raw_input("Introduce el password: ")
        print("Se han guardado los siguientes datos:\n La cuenta: %s.\nUsuario: %s.\nPassword:%s\n"%(Cuenta,Usuario,Password))
        ## ESCRITURA DE ELEMENTOS EN UN ARCHIVO
        Fichero.write(Cuenta.capwords())
        Fichero.write(";")
        Fichero.write(Usuario)
        Fichero.write(";")
        Fichero.write(Password)
        Fichero.write(";")
        Fichero.write("\n")
        print("Se han terminado de agregar los datos")
        Fichero.close() # Cierra el archivo que se abrio



    def listar(self):

        print("Ha seleccionado Listar.")
        Fichero = open("Login.csv",'r')      # Se abre el archivo de texto Hola.txt (Ruta Relativa)

        while 1:
            linea=Fichero.readline()
            if linea=="": # if linea ==""
                break
            print(linea.strip())
        print("")

    def buscar(self):
        print("Ha seleccionado Buscar.")

    def eliminar(self):
        print("Ha seleccionado Eliminar.")

    def salir(self):
        print("Ha seleccionado salir.")
        exit()




