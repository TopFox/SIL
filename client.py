import socket
from _thread import *
from threading import Thread, Event

class clientThread(Thread):
    def __init__(self, event, connection):
        Thread.__init__(self)
        self.stopped = event
        self.connection = connection
        self.client_id = 0

    def set_id(self, client_id):
        self.client_id = client_id

    def run(self):
        while not self.stopped.wait(1):
            message = 'Client ' + str(self.client_id)
            self.connection.send(str.encode(message))
        self.connection.send(str.encode('stop'))


clientConnection = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    clientConnection.connect((host, port))
    print('Successfully connected to the server')
except socket.error as e:
    print(str(e))

stopFlag = Event()
thread = clientThread(stopFlag, clientConnection)

print('Please enter your id:')
client_id = input()
thread.set_id(client_id)
while True:
    command = input()
    if command == 'start':
        thread.start()
    elif command == 'stop':
        stopFlag.set()
        print('Client stopped')
        exit()

