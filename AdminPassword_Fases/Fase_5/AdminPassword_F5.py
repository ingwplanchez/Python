import Modulo

def Main():
    Objeto = Modulo.Administrar() # Instanciacion de un objeto de la clase
                              # dentro de un modulo Administrar()
                              # Sitaxis:
                              #     Objeto = Modulo.Clase

    Objeto.Menu() # Lamada del Super Metodo Menu() que esta contenido
              # dentro de un modulo y la clase Administrar

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


###############################################################################
# LLamada a la funcion principal del programa
Main()