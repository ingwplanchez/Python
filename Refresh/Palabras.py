
cadena =raw_input("Escribe una frase. ")
a= '    '

while cadena != '':
    cambios = 0
    anterior =''
    vacios=0
    i=0

    for caracter in cadena:
        if caracter == ' ':
            vacios +=1
            #print(vacios)

        if caracter == ' ' and anterior !=' ':
            cambios +=1
        i+=1
        anterior = caracter


    if cadena[-1]==' ':
        cambios -=1

    if vacios == i:
        print("No hay palabras")
    else:
        palabras = cambios +1
        print('Palabras: ',palabras)

    cadena =raw_input("Escribe una frase. ")