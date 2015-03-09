#-------------------------------------------------------------------------------
# Name:        Program_36_Num_Espacios_En_Blanco
# Purpose:  Programa que muestra el numero de espacios de una cadena y muestra
#         el numero de espacios en blanco que contiene
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
    print frase[i]
    if frase[i]== ' ':
        j=j+1
        print j
print('El numero de espacios en blanco es: '),j
