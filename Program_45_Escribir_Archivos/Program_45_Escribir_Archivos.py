
#-------------------------------------------------------------------------------
# Name:     Program_45_Escribir_Archivo
# Purpose:  Escribir y añadir elementos a un archivo.
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     07/05/2013
#-------------------------------------------------------------------------------


Agenda = open("AgendaTelefonica.csv",'a')       # Se abre el archivo Para escribir y
                                                # Y se agrega el contenido q se le escriba
                                                # al archivo Sin Borrar lo anterior ('a')
## Agenda = open("AgendaTelefonica.csv",'w')    # Abre el archivo y borra el contenido
                                                # Para escribir nueva informacion

Nombre = input("Introduce el nombre: ")
Telefono = input("Introduce el numero de telefono: ")

print("\nSe ha guardado en la agenda el contacto: %s.\nCon su numero de tlf: %s.\n"%(Nombre,Telefono))

## ESCRITURA DE ELEMENTOS EN UN ARCHIVO

Agenda.write(Nombre)
Agenda.write(",")
Agenda.write(Telefono)
Agenda.write(",")
Agenda.write("\n")

Agenda = open("AgendaTelefonica.csv") # Abre el archivo solo para leer

## LECTURA DE ELEMENTOS EN UN ARCHIVO

## FORMA1: Bucle For

for i in range (0,9): # Para i en un rango de 0 a 9 hacer (10 Valores)
    print(Agenda.readline()) #Imprime en pantalla una linea del archivo
print("He terminado de leer el archivo")


## FORMA2: Bucle While
## Numero = 0
##while Numero>9:
##   print(Agenda.readline()) #Imprime en pantalla una linea del archivo
##   Numero = Numero + 1
##print("He terminado de leer el archivo")

Agenda.close()


