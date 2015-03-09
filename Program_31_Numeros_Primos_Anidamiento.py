#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James Marshall
#
# Created:     21/04/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

limite = int(raw_input('Dame un mumero:'))

for num in range(1, limite +1):
    creo_que_es_primo= True
    for divisor in range(2,num):
        if num%divisor==0:
            creo_que_es_primo = False
            break

        if creo_que_es_primo:
            print num

