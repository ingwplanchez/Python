import time
import thread

def imprimir(mensaje):
    while True:
        print(mensaje)
        time.sleep(1)

def main():
    mensaje="Thread1"
    mensaje2="Thread2"
    thread.start_new_thread(imprimir,(mensaje,))
    thread.start_new_thread(imprimir,(mensaje2,))
    x = raw_input("Stoy esperando que presiones enter: \n")
    print("Fin de la funcion main")

main()
