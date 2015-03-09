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

i=0
print''
numero= int(raw_input('Intruduce el numero a elevar :'))
print''

while i <= 100:
    for potencia in[i]:
        resultado= numero ** potencia
        print'%d elevado a %d es %d'%(numero,potencia,resultado)
        i= i+1