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

# Comparar 3 numeros y decir cual es el mayor

a= float(raw_input('Introduce el 1? numero'))
b= float(raw_input('Introduce el 2? numero'))
c= float(raw_input('Introduce el 3? numero'))

if a>b and a>c:
    maximo = a

if b>a and b>c:
    maximo = b

if c>a and c>b:
    maximo = c

print('El numero maximo es: '),maximo