#-------------------------------------------------------------------------------
# Name:        Program_38_Num_De_Digitos
# Purpose:  Programa que lee una cadena y muestra el numero de Digitos que
#        posee, ademas de indicar si no posee digitos.
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     11/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

frase = raw_input('Introduce una frase ')
print' '
print frase
print' '

j=0
for i in range(len(frase)):

    if frase[i] <= '9'  and frase[i] >= '0' :  # a-z (97-122)
        j=j+1

if j!=0:
    print'La Cantidad de digitos de la frase es, %d'%(j)
else:
    print'La frase no posee digitos'

