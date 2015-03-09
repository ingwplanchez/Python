#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James Marshall
#
# Created:     15/04/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import pi

radio = float(raw_input('Dame el radio de un circulo: '))

#Menu

print 'Escoge una opcion:'
print ' '
print 'a) Calcular el diametro.'
print 'b) Calcular el perimetro.'
print 'c) Calcular el area.'
print ' '

opcion= raw_input('Teclea la opcion y pulsa Enter: ')

if opcion == 'a' or opcion == 'A':
    diametro = 2*radio
    print 'El diametro es', diametro

else:
    if opcion == 'b' or opcion == 'B':
        perimetro = 2*pi*radio
        print 'El perimetro es', perimetro

    else:
        if opcion == 'c' or opcion == 'C':
            area = pi*radio**2
            print 'El area es', area

