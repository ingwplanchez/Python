#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James Marshall
#
# Created:     19/04/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

print'Imprimir los numeros pares entre 0 y 200 de forma creciente'

for pares in range(0,201):
    if pares == int(pares/2)*2 and pares>0:
        print pares