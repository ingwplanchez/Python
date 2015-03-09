
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




