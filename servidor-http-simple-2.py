#!/usr/bin/python3

"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1235))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        print (recvSocket.recv(2048))
        print ('Answering back...')
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", 'utf-8') +
                        bytes("<html><body><h1>Que pasa bros<3</h1></body></html>", 'utf-8') +
                        bytes("<h1> A hackear un poco la cyber web</h1>", 'utf-8')+
                        bytes("<p><font size='10'>Yano hay más. Os dejo un pengolin <p/>", 'utf-8')+
                        bytes("<img src='https://assets.pcmag.com/media/images/532520-pangolin-v-day-google-doodle.jpg?thumb=y&width=810&height=455' width='810' height='455'>", 'utf-8')+
                        bytes("\r\n", 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
