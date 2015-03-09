#-------------------------------------------------------------------------------
# Name:       Program_37_Num_De_Mayusculas
# Purpose:  Programa que lee una cadena y muestra el numero de letras
#        may?sculas que contiene.
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

    if frase[i] <= 'z'  and frase[i] >= 'a':  # a-z (97-122)
        print frase[i], 'La letra es minuscula'

    if frase[i] <= 'Z' and frase[i] >= 'A':  # A-Z (65-90)
        print frase[i], 'La letra es mayuscula'
        j=j+1
print('El numero de Mayusculas : '),j

