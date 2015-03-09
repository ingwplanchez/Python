
#-------------------------------------------------------------------------------
# Name:     Program_44_Leer_Archivo
# Purpose:  Abrir y leer un archivo de texto (.txt)
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     07/05/2013
#
#-------------------------------------------------------------------------------

# Texto = open("Archivo.txt")           # Se abre el archivo de texto Hola.txt (Ruta Absoluta)
Texto = open("Documentos/Hola.txt")     # Se abre el archivo de texto Hola.txt (Ruta Relativa)
print(Texto.read())                     # Lee el contenido de u archivo de texto
                                        # Y lo muestra en pantalla







