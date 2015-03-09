
def Bienvenidos(): # def se utiliza para definir una funcion

    print("Bienvenido a la agenda telefonica.\n")
    print("1.- Agregar un elemento a la agenda.")
    print("2.- Listar los elementos de la agenda.")
    print("3.- Buscar por nombres.")
    print("4.- Salir.")

def Escribir():

    print("Has elegido agregar un elemento a la agenda.\n")

##  Posicion = input("Introduce una posicion:")
    Nombre = input("Introduce el nombre: ")
    Telefono = input("Introduce el numero de telefono: ")

    ## APERTURA DE UN ARCHIVO PARA AGREGAR ELEMENTOS
    Agenda = open("agendatelefonica.csv")   # Se abre el archivo Para escribir y
                                                # Y se agrega el contenido q se le escriba
                                                # al archivo Sin Borrar lo anterior ('a')

    for n in range(1,40):
        Linea = Agenda.readline()
        LineaPartida = Linea.split(",") # Convierte un string en una lista
        ## print(LineaPartida[0]) # Imprime los incices
        if LineaPartida[0] != "": # Si el indice esta vacio
            Memoria = LineaPartida[0] #
    ## print("El numero maximo de memoria es:",Memoria)
    Agenda.close()
    MemoriaInt = int(Memoria)
    Posicion = 0
    Posicion = MemoriaInt + 1
    Postr = str(Posicion)
    print("Se ha guardado en la agenda el contacto: %s.\nCon su numero de tlf: %s.\n"%(Nombre,Telefono))
    ## ESCRITURA DE ELEMENTOS EN UN ARCHIVO
    Agenda = open("agendatelefonica.csv","a")
    Agenda.write(Postr)
    Agenda.write(",")
    Agenda.write(Nombre)
    Agenda.write(",")
    Agenda.write(Telefono)
    Agenda.write(",")
    Agenda.write("\n")
    print("Se han terminado de agregar los datos")
    Agenda.close() # Cierra el archivo que se abrio

def Consulta(fin):

    print("Has elegido listar los elementos de la agenda.\n")
    ## APERTURA DE UN ARCHIVO PARA LEER ELEMENTOS
    Agenda = open("agendatelefonica.csv")
    Numero = 0
    while Numero<fin:
       Formato = Agenda.readline()
       print(Formato.replace(",","\t\t")) # Se reemplaza un valor por otro
       Numero = Numero + 1
    print("He terminado de leer el archivo")
    Agenda.close() # Cierra el archivo que se abrio

def MiError():

    print("La opcion no es valida.")

def Buscador(NombreBuscado):

    print("Aqui se buscaran los contactos.")
    Agenda = open("agendatelefonica.csv")

    for i in range(1,30):
        Lectura = Agenda.readline()
        Partido = Lectura.split(',') # Convierte un string en una lista
        if NombreBuscado == Partido[1]: # Si el Nombre buscado coincide
            print(Partido[2]) # Imprime el numero en pantalla

    Agenda.close() # Cierra el archivo que se abrio



