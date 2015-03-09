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

# Dados 5 numeros enteros, determinar cual de los 4 numeros enteros es mas
# cercano al primero.

a= int(raw_input('Introduce el Primer numero'))
b= int(raw_input('Introduce el Segundo numero'))
c= int(raw_input('Introduce el Tercer numero'))
d= int(raw_input('Introduce el Cuarto numero'))
e= int(raw_input('Introduce el Quinto numero'))

Resta1= a - b
Resta2= a - c
Resta3= a - d
Resta4= a - e

menor_diferencia = Resta1

if Resta2 < menor_diferencia and Resta2 >= 0:
   menor_diferencia = Resta2

else:
    if Resta2 > menor_diferencia and Resta2 <= 0:
        menor_diferencia = Resta2

if Resta3 < menor_diferencia and Resta3 >= 0:
   menor_diferencia = Resta3

else:
    if Resta3 > menor_diferencia and Resta3 <= 0:
        menor_diferencia = Resta3

if Resta4 < menor_diferencia and Resta4 >= 0:
   menor_diferencia = Resta4

else:
    if Resta4 > menor_diferencia and Resta4 <= 0:
        menor_diferencia = Resta4

numero_cercano= a - menor_diferencia

print 'El numero mas cercano a %d es %d'%(a,numero_cercano)





