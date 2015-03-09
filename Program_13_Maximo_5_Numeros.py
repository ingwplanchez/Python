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

def main():
    pass

if __name__ == '__main__':
    main()

# Calcular el maximo de 5 n?meros

a= float(raw_input('Introduce el Primer numero'))
b= float(raw_input('Introduce el Segundo numero'))
c= float(raw_input('Introduce el Tercer numero'))
d= float(raw_input('Introduce el Cuarto numero'))
e= float(raw_input('Introduce el Quinto numero'))

posible_maximo = a

if b > posible_maximo:
    posible_maximo = b

if c > posible_maximo:
    posible_maximo = c

if d > posible_maximo:
    posible_maximo = d

if e > posible_maximo:
    posible_maximo = e

maximo = posible_maximo

print 'El Numero maximo es', maximo