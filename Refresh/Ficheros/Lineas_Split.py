try:
    # Se abre el archivo de texto Hola.txt (Ruta Relativa)
    Fichero = open("Documentos/Fichero.txt",'r')
except:
    print("El Archivo no existe.")
else:
    for linea in Fichero:
        partir = linea.split()
        print(partir)
        print("elementos en la Lista",len(partir))
        print linea.strip()
        print("")
    Fichero.close()
