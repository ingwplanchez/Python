import Modulo

###############################################################################

Modulo.Menu() # Lamada del Super Metodo Menu() que esta contenido
              # dentro de un modulo y la clase Administrar

opcion = raw_input("Introduce una opcion del menu: ")
print("")

if opcion =='1':
    Modulo.agregar()  # Llamada al metodo agregar() dentro de la clase

elif opcion =='2':
    Modulo.listar()   # Llamada al metodo listar() dentro de la clase

elif opcion =='3':
    Modulo.buscar()   # Llamada al metodo buscar() dentro de la clase

elif opcion =='4':
    Modulo.eliminar() # Llamada al metodo eliminar() dentro de la clase

elif opcion =='5':
     Modulo.salir()   # Llamada al metodo salir() dentro de la clase

else:
    print("La opcion no es valida.\n")