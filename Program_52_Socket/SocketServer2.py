#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anonymous
#
# Created:     16/05/2014
# Copyright:   (c) Anonymous 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import SocketServer

class MiTcpHandler(SocketServer.BaseRequestHandler):

    #def __init__(self):
        #super(MiTcpHandler, self).__init__()
    def handle(self):
        self.oracion=self.request.recv(1014).strip()
        self.num = len(self.oracion)
        print "La oracion recv es ",self.oracion," el numero de caracteres " ,self.num
        self.request.send(str(self.num)) # envia el numero

def main():
    print "Servidores"
    host = "localhost" #Direccion
    port = 9999
    server1 = SocketServer.TCPServer((host,port),MiTcpHandler)
    print("Servidor Activo")
    server1.serve_forever() #Servidor activo hasta que se cierra el programa

main()