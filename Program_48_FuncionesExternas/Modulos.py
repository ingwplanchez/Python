
def Bienvenidos(): # def se utiliza para definir una funcion
    
    print("Bienvenido a la agenda telefonica.\n")
    print("1.- Agregar un elemento a la agenda")
    print("2.- Listar los elementos de la agenda")
    print("3.- Buscar por nombres\n")

def Escribir():
    
    print("Has elegido agregar un elemento a la agenda.\n")
    ## APERTURA DE UN ARCHIVO PARA AGREGAR ELEMENTOS
    Agenda = open("AgendaTelefonica.csv",'a')   # Se abre el archivo Para escribir y
                                                # Y se agrega el contenido q se le escriba
                                                # al archivo Sin Borrar lo anterior ('a')
    Posicion = input("Introduce una posicion:")                                        
    Nombre = input("Introduce el nombre: ")
    Telefono = input("Introduce el numero de telefono: ")
    print("Se ha guardado en la agenda el contacto: %s.\nCon su numero de tlf: %s.\n"%(Nombre,Telefono))
    ## ESCRITURA DE ELEMENTOS EN UN ARCHIVO
    Agenda.write(Posicion)
    Agenda.write(";")
    Agenda.write(Nombre)
    Agenda.write(";")
    Agenda.write(Telefono)
    Agenda.write(";")
    Agenda.write("\n")
    print("Se han terminado de agregar los datos")
    Agenda.close() # Cierra el archivo que se abrio
  
def Consulta(fin):
    
    print("Has elegido listar los elementos de la agenda.\n")
    ## APERTURA DE UN ARCHIVO PARA LEER ELEMENTOS
    Agenda = open("AgendaTelefonica.csv")
    Numero = 0
    while Numero<fin:
       Formato = Agenda.readline() 
       print(Formato.replace(";","\t\t")) # Se reemplaza un valor por otro
       Numero = Numero + 1
    print("He terminado de leer el archivo")
    Agenda.close() # Cierra el archivo que se abrio

def MiError():
    
    print("La opcion no es valida.")
    
def Buscador():
    
    print("Aqui se buscaran los contactos.")

