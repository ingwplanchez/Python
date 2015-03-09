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

sumatoria = 0
i = int(raw_input('Introduce el numero desde el cual desea sumar: '))
limite= int(raw_input('Introduce el numero hasta el cual de sea sumar: '))
while i <= limite:
    i = i + 1
    sumatoria = sumatoria = sumatoria + i

print 'La sumatoria es',sumatoria

