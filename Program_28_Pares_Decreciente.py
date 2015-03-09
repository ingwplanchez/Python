#-------------------------------------------------------------------------------
# Name:        module2
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

print'Imprimir los numeros pares entre 0 y 200 de forma decreciente'

for pares in range(200,-1,-1):
    if pares == int(pares/2)*2 and pares>0:
        print pares