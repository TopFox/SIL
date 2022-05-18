import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')

ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    connectionAlive = True
    while connectionAlive:
        data = connection.recv(2048)
        data = data.decode('utf-8')
        if data == 'stop':
            print('Connection with client closed')
            connection.close()
            connectionAlive = False
        else:
            print(data)


while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
ServerSideSocket.close()