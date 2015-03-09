#-------------------------------------------------------------------------------
# Name:        Program_40_Lista_Variable
# Purpose:  Programa que almacena en una variable (a) la lista obtenida con
# range(1,4), y a continuacion la modifique, para que cada componente sea
# igual al cuadrado del n?mero entero original. El programa Mostrar? la lista
# reusltante por pantalla.
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     16/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

a =  range(1,4)
print 'Antes',a
i= 0
while i < 3:

    a[i] = a[i]**2
    i= i+1
print 'Despues',a

