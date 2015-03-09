
#-------------------------------------------------------------------------------
# Name:     Program_48_FuncionesExternas
# Purpose:  Mostrar como externalizan las funciones, y se crean modulos
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     08/05/2013
#-------------------------------------------------------------------------------

import Modulos

Modulos.Bienvenidos()
Opcion = raw_input("Seleccione una opcion: ")
print(" ")

## ESTRUCTURAS DE DESICION

if Opcion == '1':

    Modulos.Escribir()

elif Opcion == '2':

    Registros = raw_input("Dime cuantos registros quieres ver: ")
    RegistrosInt = int(Registros)
    Modulos.Consulta((RegistrosInt))

else:

    Modulos.MiError()

exit
