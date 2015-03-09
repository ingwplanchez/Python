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

print''
numero= int(raw_input('Intruduce el numero a elevar :'))
print''

for potencia in range(0,101):
    resultado= numero ** potencia
    print'%d elevado a %d es %d'%(numero,potencia,resultado)
