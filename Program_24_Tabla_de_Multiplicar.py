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


i=0
print''
numero= int(raw_input('De que numero desea saber la tabla de multiplicar? :'))
print''

while i <= 10:

    for multiplicador in[i]:
        resultado= numero * multiplicador
        print'%d x %d = %d'%(numero,multiplicador,resultado)
        i= i+1


