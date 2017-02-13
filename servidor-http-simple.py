#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
# tenemos que convertir el string en bytes
# la función bytes (string, 'codificacion') lo hace
# HTML-->
# <h1> es como head o algo así
#<p> es parrafo (esa si xd)
#<img src = 'url' width = ''> etc
while True:
    print ('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print ('HTTP request received:')
    print (recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", 'utf-8') +
                    bytes("<html><body><h1>Que pasa bros<3</h1></body></html>", 'utf-8') +
                    bytes("<h1> A hackear un poco la cyber web</h1>", 'utf-8')+
                    bytes("<p><font size='10'>Yano hay más. Os dejo un pengolin <p/>", 'utf-8')+
                    bytes("<img src='https://assets.pcmag.com/media/images/532520-pangolin-v-day-google-doodle.jpg?thumb=y&width=810&height=455' width='810' height='455'>", 'utf-8')+
                    bytes("\r\n", 'utf-8'))
    recvSocket.close()
