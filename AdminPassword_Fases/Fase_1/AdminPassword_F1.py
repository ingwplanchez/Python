
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

    def listar(self):
        print("Ha seleccionado Buscar.")

    def buscar(self):
        print("Ha seleccionado Buscar.")

    def eliminar(self):
        print("Ha seleccionado Eliminar.")

    def salir(self):
        print("Ha seleccionado salir.")

###############################################################################
# Funcion principal del programa

def Main():
    Objeto = Administrar() # Instanciacion de un objeto de la clase Administrar()
    Objeto.Menu() # Lamada del Super Metodo Menu()

    opcion = raw_input("Introduce una opcion del menu: ")
    print("")

    if opcion =='1':
        Objeto.agregar()  # Llamada al metodo agregar() dentro de la clase
        Main()

    elif opcion =='2':
        Objeto.listar()   # Llamada al metodo listar() dentro de la clase
        Main()

    elif opcion =='3':
        Objeto.buscar()   # Llamada al metodo buscar() dentro de la clase
        Main()

    elif opcion =='4':
        Objeto.eliminar() # Llamada al metodo eliminar() dentro de la clase
        Main()

    elif opcion =='5':
        Objeto.salir()   # Llamada al metodo salir() dentro de la clase
        Main()

    else:
        print("La opcion no es valida.\n")
        exit

###############################################################################
# LLamada a la funcion principal del programa
Main()