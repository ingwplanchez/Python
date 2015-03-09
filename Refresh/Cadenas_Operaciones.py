print("De cadenas a listas:")
Cadena1 = "Uno Dos Tres"
print(Cadena1)
A= Cadena1.split()
print(A)
print("")

Cadena2= "Uno:Dos:Tres"
print("Funcion Split con un caracter Divisor: ")
print(Cadena2)
B= Cadena2.split(':')
print(B)
print("")

D = ['0','2','4']
print("Unir los elementos de una lista en una cadena indicando un separador: _")
print(D)
F = '_'.join(D)
print(F)
print('')

print("Algo mas sobre listas: se le puede aplicar el metodo len()")
Lista= "elemento1 elemento2 elemento3"
Expandir = Lista.split()
print(Expandir)
print("Elementos en la lista",len(Expandir))

print("")
Nueva_Cadena="Hola esto es una prueba del metodo replace"
print("Antes de replace")
print(Nueva_Cadena)
print("")

print("Despues de replace.Los espacios en blanco cambian por :")
Cadena_Modificada=Nueva_Cadena.replace(" ",":")
print(Cadena_Modificada)



