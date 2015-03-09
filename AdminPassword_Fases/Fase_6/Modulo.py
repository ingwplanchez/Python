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

        Cuenta = raw_input("Introduce a que cuenta pertenece el login: ")
        Usuario = raw_input("Introduce el nombre de usuario: ")
        Password = raw_input("Introduce el password: ")

        ## APERTURA DE UN ARCHIVO PARA AGREGAR ELEMENTOS
        Fichero = open("Login.csv")   # Se abre el archivo Para escribir y
                                                # Y se agrega el contenido q se le escriba
                                                # al archivo Sin Borrar lo anterior ('a')
        for n in range(1,40):
            Linea = Fichero.readline()
            LineaPartida = Linea.split(";") # Convierte un string en una lista

            ## print(LineaPartida[0]) # Imprime los incices

            if LineaPartida[0] != "": # Si el indice esta vacio
                Memoria = LineaPartida[0]
                print(Memoria)

        ## print("El numero maximo de memoria es:",Memoria)
        Fichero.close()
        try:
            Posicion = 0
            MemoriaInt = int(Memoria)

            Posicion = MemoriaInt + 1
            Postr = str(Posicion)
        except UnboundLocalError:
            Postr = '1'

        ## APERTURA DE UN ARCHIVO PARA AGREGAR ELEMENTOS
        Fichero = open("Login.csv",'a')   # Se abre el archivo Para escribir y
                                                    # Y se agrega el contenido q se le escriba
                                                    # al archivo Sin Borrar lo anterior ('a')

        ## ESCRITURA DE ELEMENTOS EN UN ARCHIVO

        Fichero.write(Postr)
        Fichero.write(";")
        Fichero.write(Cuenta)
        Fichero.write(";")
        Fichero.write(Usuario)
        Fichero.write(";")
        Fichero.write(Password)
        Fichero.write("\n")

        print("Se han guardado los siguientes datos:\n La cuenta: %s.\nUsuario: %s.\nPassword:%s\n"%(Cuenta,Usuario,Password))
        print("Se han terminado de agregar los datos")
        Fichero.close() # Cierra el archivo que se abrio



    def listar(self):

        print("Ha seleccionado Listar.")
        print("")
        print("Indice\t\tCuenta\t\tUsuario\t\tPassword\n")
        Fichero = open("Login.csv",'r')      # Se abre el archivo de texto Hola.txt (Ruta Relativa)

        while 1:
            linea=Fichero.readline()
            if linea == "": # if linea ==""
                break
            print(linea.replace(";","\t\t"))
        print("")

    def buscar(self):
        try:
            print("Ha seleccionado Buscar.")
            print("Aqui se Mostraran los datos de las cuentas.")
            NombreBuscado = raw_input("Dime el nombre de la cuenta: ")
            Fichero = open("Login.csv")

            for i in range(1,30):

                Lectura = Fichero.readline()
                Partido = Lectura.split(';') # Convierte un string en una lista
                if NombreBuscado == Partido[1]: # Si el Nombre buscado coincide
                    #print("%s\t\t%s\t\t%s"%(Partido[1],Partido[2],Partido[3]) # Imprime el numero en pantalla
                    #print("Cuenta: ",Partido[1])
                    #print("Usuario: ",Partido[2])
                    # print("Pasword: ",Partido[3])
                    print("")

                    print(Partido[2])
                    print(Partido[3])
            Fichero.close()
        except:
            print("Busquda Finalizada")



    def eliminar(self):
        print("Ha seleccionado Eliminar.")

    def salir(self):
        print("Ha seleccionado salir.")
        exit()





