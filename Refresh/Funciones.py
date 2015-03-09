print("Ejemplo que muestra el funcionamiento de las Funciones.")

#Funcion sin argumentos
def mensaje1():
    print("Hola esto es una funcion que muestra un mensaje")
    print("")
def mensaje2():
    print("Hola esto es una funcion que muestra otro mensaje")
    print("")

# funcion con parametros
def suma(num1=0,num2=0):
    print("Funcion con 2 parametros:")
    Resultado=num1+num2
    return Resultado


# Funcion con argumentos variables *args
def varios(num1,num2,*args):
    for Elementos in args:
        print Elementos

mensaje1()
mensaje2()

print("El sesultado de la suma es %d"%(suma(45,6)))


print("")
print("Funcion con un numero variable de argumentos:")

varios(1,2,3,4,5,6)

