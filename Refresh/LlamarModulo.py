import Modulo

#LLamada de Funciondes desde Otro Modulo
print("LLamada de Funciondes desde Otro Modulo.")
Modulo.mi_funcion()
Modulo.mi_funcion2()
print("")

print("Llamada de una clase desde otro modulo.")
#Instanciacion del objeto de la clase contenida en el modulo
Objeto = Modulo.MiClase()
Objeto.Mensaje()