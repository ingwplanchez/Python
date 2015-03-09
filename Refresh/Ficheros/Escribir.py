
Fichero = open("Documentos/Escribir2.txt","w")
contenido1 = "Este contenido se escribe en el archivo."
contenido2 = "Tambien se agrega este contenido"
Fichero.write(contenido1)
Fichero.write(".")
Fichero.write("\n")
Fichero.write(contenido2)
Fichero.write(".")
Fichero.write("\n")
Fichero.close()

Fichero = open("Documentos/Escribir2.txt","r")
print("Contenido actual de la agenda despues de escribir: ")
print("")
print(Fichero.read())                     # Lee el contenido de un archivo de texto
                                          # Y lo muestra en pantalla
Fichero.close()