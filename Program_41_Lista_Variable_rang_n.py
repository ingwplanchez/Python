#-------------------------------------------------------------------------------
# Name:        Program_41_Lista_Variable_rang_n
# Purpose:  Programa que almacena en una variable (a) la lista obtenida con
# range(1,n), donde n es un entero que se pide al usuario y modifique dicha
# para que cada componente sea igual al cuadrado del componente original. El
# Programa mostrar? la lista  reusltante por pantalla.
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

n= int(raw_input('Introduce un numero'))
a =  range(1,n)
n = n - 1
print('Antes',a)
i= 0
while i < n:

    a[i] = a[i]**2
    i= i+1
print ('Despues',a)
