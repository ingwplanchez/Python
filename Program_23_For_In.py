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

print 'Introduce 3 nombres.'
print''

a= raw_input('Introduce el Primer nombre nombre:')
b= raw_input('Introduce el Segundo nombre nombre:')
c= raw_input('Introduce el Tercer nombre nombre:')

for nombre in [a,b,c]:
    print'Hola, %s' %nombre

print''
numero= int(raw_input('Introduce introduce un numero'))
print''

for potencia in[2,3,4,5]:
    print '%d elevado a %d es %d' %(numero,potencia,numero**potencia)

