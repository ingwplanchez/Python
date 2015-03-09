#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James Marshall
#
# Created:     18/04/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from math import pi

continuar = 's'
opcion = ''

#Menu


while opcion <'a' or opcion >'c':

    if continuar == 's' or continuar =='S':

        print''
        radio = float(raw_input('Dame el radio de un circulo: '))
        print''
        print 'Escoge una opcion:'
        print ' '
        print 'a) Calcular el diametro.'
        print 'b) Calcular el perimetro.'
        print 'c) Calcular el area.'
        print 'd) Salir.'

        print ' '
        opcion= raw_input('Teclea la opcion y pulsa Enter: ')
        print''

        if opcion == 'a' or opcion == 'A':
            diametro = 2*radio
            print 'El diametro es', diametro,'metros'


        elif opcion == 'b' or opcion == 'B':
            perimetro = 2*pi*radio
            print 'El perimetro es', perimetro, 'metros'

        elif opcion == 'c' or opcion == 'C':
            area = pi*radio**2
            print 'El area es', area,'metros cuadrados'

        elif opcion == 'd' or opcion == 'D':
            exit()

        else:
            print'Solo hay 4 opciones a,b,c y d',
            print 'Tu has tecleado: ', opcion
            opcion=''

        continuar= ''

        while continuar=='':
            print''
            print'Desea continuar con la ejecucion del programa?'
            print''
            continuar= raw_input('Continuar Si(s)- No(n): ')
            print''


            if continuar == 's':
                opcion= ''

            if continuar == 'n':
                print''
                print 'Programa terminado, Hasta la proxima'


            if continuar < 'n'  or continuar > 's':
                print''
                print 'El Valor',continuar, 'No es una opcion valida.'
                continuar= ''








