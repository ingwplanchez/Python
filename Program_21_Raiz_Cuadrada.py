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

from math import sqrt

x = float(raw_input('Introduce un numero positivo: '))
if x< 0:
    print 'El numero no es positivo'
    x = float(raw_input('Introduce un numero positivo: '))

print'La raiz cuadrada de %1.2f es %1.2f'%(x,sqrt(x))