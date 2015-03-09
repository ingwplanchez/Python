

def Menu():       # Super metodo Menu. este llama a otros metodos

    print("Bienvenido@ a la aplicacion.\n")
    print("Seleccione una Opcion del Menu: \n")

    print("1.- Agregar.")
    print("2.- Listar.")
    print("3.- Buscar.")
    print("4.- Eliminar.")
    print("5.- Salir.\n")

def agregar():
   print("Ha seleccionado Agregar.")

def listar():
    #print("Ha seleccionado listar.")

    Texto = open("Login.txt")      # Se abre el archivo de texto Hola.txt (Ruta Relativa)
    print(Texto.read())                     # Lee el contenido de un archivo de texto
                                    # Y lo muestra en pantalla
    Texto.close()


def buscar():
    print("Ha seleccionado Buscar.")

def eliminar():
    print("Ha seleccionado Eliminar.")

def salir():
    print("Ha seleccionado salir.")





