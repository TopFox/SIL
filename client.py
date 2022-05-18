import socket
from _thread import *
from threading import Thread, Event

class MyThread(Thread):
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


ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
stopFlag = Event()
thread = MyThread(stopFlag, ClientMultiSocket)

print('Please enter your client_id:')
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

