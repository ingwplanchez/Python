
Fichero = open("Documentos/Escribir.txt","a")
contenido1 = "Este contenido se sobre-escribe en el archivo."
contenido2 = "Tambien esto se sobre-escribe este contenido"
Fichero.write(contenido1)
Fichero.write(".")
Fichero.write("\n")
Fichero.write(contenido2)
Fichero.write(".")
Fichero.write("\n")
Fichero.close()

Fichero = open("Documentos/Escribir.txt","r")
print("Contenido actual de la agenda despues de escribir: ")
print("")
print(Fichero.read())                     # Lee el contenido de un archivo de texto
                                          # Y lo muestra en pantalla
Fichero.close()