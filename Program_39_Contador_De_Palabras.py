#-------------------------------------------------------------------------------
# Name:        Program_39_Contador_De_Palabras
# Purpose:  Contar el numero de palabras de una frase
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     11/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

cadena = raw_input('Escribe una frase: ')
while cadena !='': #En caso de pulsar enter finaliza el programa
    cambios = 0
    anterior =' '
    for caracter in cadena:
        if caracter==' 'and anterior !=' ':#Dentro del Bucle For
            cambios=cambios + 1
        anterior = caracter

    if cadena[-1]==' ': #Fuera del bucle For
        cambios = cambios - 1

    palabras= cambios + 1
    print 'Palabras:',palabras
    cadena = raw_input('Escribe una frase: ')


