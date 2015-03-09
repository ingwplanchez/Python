# -*- coding: utf-8 -*-

# Parametros para Trabajar con ficheros

#Funcion open(Argumento1,Argumento2)
#Los Argumentos se colocan como String es decir entre comillas ""
#El Argumento1 es la ruta absoluta o relativa del archivo
#El Argumento2 es opcional y puede ser:

    #'r':read,lectura.Abre el archivo en modo lectura. Si no existe
    # se genera un error.

    #'w':write,escritura.Abre un archivo en modo escritura. Si el archivo
    # no existe se crea. Sobre escribe la informacion.

    ##'a':append,añadir. Abre el archivo en modo escritura. No sobreescribe
    ## la informacion.

    #'+':permite lectura y escritura simultaneas


try:
    # Se abre el archivo de texto Hola.txt (Ruta Relativa)
    Fichero = open("Documentos/Fichero.txt",'r')
except:
    print("El Archivo no existe.")
else:
    while 1:
        linea=Fichero.readline()
        if not linea: # if linea ==""
            break
        print(linea.strip())

    Fichero.close()

