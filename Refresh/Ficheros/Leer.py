# -*- coding: utf-8 -*-


Texto = open("Documentos/Fichero.txt")      # Se abre el archivo de texto Hola.txt (Ruta Relativa)
print(Texto.read())                     # Lee el contenido de un archivo de texto
                                        # Y lo muestra en pantalla
Texto.close()