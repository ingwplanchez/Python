from math import pi

radio = float(raw_input('Dame el radio de un circulo: '))
print ' '

#Menu

print 'Escoge una opcion:'
print ' '
print 'a) Calcular el diametro.'
print 'b) Calcular el perimetro.'
print 'c) Calcular el area.'
print ' '

opcion= raw_input('Teclea la opcion y pulsa Enter: ')

if opcion == 'a' or opcion == 'A':
    diametro = 2*radio
    print ' '
    print 'El diametro es', diametro

else:
    if opcion == 'b' or opcion == 'B':
        perimetro = 2*pi*radio
        print ' '
        print 'El perimetro es', perimetro

    else:
        if opcion == 'c' or opcion == 'C':
            area = pi*radio**2
            print ' '
            print 'El area es', area

        else:
            print 'Solo hay 3 opciones, a , b o c.'
            print' '
            print 'Tu has tecleado: ', opcion











