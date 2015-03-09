7#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James Marshall
#
# Created:     20/04/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

num= int(raw_input('Dame un numero :'))

creo_q_es_primo = True
divisor=2

while divisor < num:
    if num % divisor == 0:
        creo_q_es_primo= False
        break
    divisor += 1

if creo_q_es_primo:
    print' El numero',num,'es primo'

else:
    print' El numero',num,' No es primo'



