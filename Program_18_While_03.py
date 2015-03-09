#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      James Marshall
#
# Created:     17/04/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
i = int(raw_input('Valor inicial'))
limite = int(raw_input('Limite'))
incremento = int(raw_input('Incremento'))

while i <= limite:
    print i
    i=i+incremento
print' '
print'Hecho'