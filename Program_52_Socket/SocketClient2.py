'''
Created on 18/05/2014

@author: Anonymous
'''
import socket
print("Prueba Socket Cliente")
host ="localhost"
port = 9999
socket1=socket.socket()
socket1.connect((host,port))
oracion = raw_input("Ingrese oracion: ")
socket1.send(oracion)
numero = socket1.recv(1024)
print("la oracion ",oracion,"tiene caracteres: ",numero)
tiempo = raw_input("presiene enter para salir . . . ")
socket1.close()
