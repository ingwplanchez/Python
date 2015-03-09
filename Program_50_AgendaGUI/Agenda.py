
#-------------------------------------------------------------------------------
# Name:     Program_49_Listas
# Purpose:  Mostrar como externalizan las funciones, y se crean modulos
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     08/05/2013
#-------------------------------------------------------------------------------

import Modulos

def Main():
    Modulos.Bienvenidos()
    Opcion = input("Seleccione una opcion: ")
    print(" ")

    ## ESTRUCTURAS DE DESICION

    if Opcion == '1':

        Modulos.Escribir()
        Main()
    elif Opcion == '2':

        Registros = input("Dime cuantos registros quieres ver: ")
        RegistrosInt = int(Registros)
        Modulos.Consulta((RegistrosInt))
        Main()
    elif Opcion == '3':

        NombreBuscado = input("Dime el nombre que estas buscando: ")
        Modulos.Buscador(NombreBuscado)
        Main()

    elif Opcion == '4':

        print('Fin del Programa.')
        exit

    else:

        Modulos.MiError()
        Main()
Main()
