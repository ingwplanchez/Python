print("Manejo de errores: ")

def division(a,b):
    return a/b

def calcular():
    print("El resultado es",division(1,0))

# Tratamiento de errores
try:
    Resultado = division(1,1)

except NameError:
    print("La variable no existe. ")
except ValueError:
    print("Uno de los valores no es un numero.")
except TypeError:
    print("Una de las variables no es un numero.")
except ZeroDivisionError:
    print("La division entre Cero no esta definida.")
else:
    print("La Division es: ",Resultado)

print("")
print("Se puede usar una tupla para listar los tipos de error:")

try:
    division('a',0)
except (NameError,ValueError,ZeroDivisionError,TypeError):
    print("Se ha generado un error")