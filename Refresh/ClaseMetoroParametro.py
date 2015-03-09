
class operaciones1:

    def __init__(self):
        pass
    # Metodo con parametros
    def suma(self,num1=0,num2=0):
        print("Metodo con 2 parametros:")
        Resultado=num1+num2
        return Resultado

class operaciones2:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        print("Objeto con dos parametros en el Metodo constructor ")
        Resultado=self.num1+self.num2
        return Resultado
Objeto = operaciones1()
Objeto2 = operaciones2(2,4)

print("El Resultado de la suma es %d"%(Objeto.suma(45,6)))
print(" ")

print("El Resultado de la suma es %d"%(Objeto2.suma()))

