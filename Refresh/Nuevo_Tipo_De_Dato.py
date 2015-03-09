
class Suma:
     def __init__(self, numero1=0,numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2

     def __str__(self):
         return "Los numeros son: %d y %d" % (self.numero1, self.numero2)

     def __int__(self):
         return self.numero1+self.numero2

Objeto = Suma(6,6)
ObjetoEntero = Suma(3,2)

print("Se imprime el objeto como un string: ")
print(Objeto)
print("")
print("El Objeto es %s"%(Objeto))

print("Se imprime el objeto como un Entero: ")
print(ObjetoEntero)
print("")
print("Objeto entero: %d"%(ObjetoEntero))


