#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James Marshall
#
# Created:     18/10/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

nombre = []
apellido = []
Cant_Productos = []
n = ' '
a = ' '
c = 0
flag= 1
k=0
i=0
while (flag==1):

    continuar = raw_input('Desea introducir nuevos datos de cliente?: ')
    if(continuar=='s' or continuar=='S'):

        n = raw_input('introduzca el nombre del cliente: ')

        a = raw_input('introduzca el apellido del cliente: ')
        c = raw_input('introduzca la antidad de productos: ')

        nombre.append(n)
        apellido.append(a)
        Cant_Productos.append(c)
        i = i + 1
    else:
        flag = 0
#n = i

print('Numero de clientes: %d\n' %i )
print('Los datos de los clientes son: \n')

for i in range(0,len(nombre)):

    k  = i + 1
    print('Cliente [%d]\nNombre: %s\t\t Apellido: %s\t\tProductos: %s\n')%(k,nombre[i],apellido[i],Cant_Productos[i])
print('Fin del programa.')
exit


