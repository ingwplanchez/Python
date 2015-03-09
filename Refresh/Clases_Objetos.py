class Clase:
    def __init__(self):
        pass
    def metodo1(self):
        print("El objeto hace uso del metodo de la clase")
        return 'hola'

class Coche:

    def __init__(self,gasolina):
        self.gasolina = gasolina
        print("tenemos",gasolina,"litros")

    def arrancar(self):
        if self.gasolina>0:
            print("Arranca")
        else:
            print("No arranca")

    def conducir(self):
        if self.gasolina>0:
            self.gasolina -= 1
            print("Quedan",self.gasolina,"litros")
        else:
            print("no se mueve")
Objeto = Clase() #instanciacion de un objeto
print (Objeto.metodo1())

Objeto2= Coche(2)
Objeto2.arrancar()
Objeto2.conducir()


