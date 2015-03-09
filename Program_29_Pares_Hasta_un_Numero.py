#-------------------------------------------------------------------------------
# Name:        module3
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
numero= int(raw_input('Hasta que numero desea que se muestren los pares? :'))
numero= numero + 1

for pares in range(0,numero):
    if pares == int(pares/2)*2 and pares>0:
        print pares