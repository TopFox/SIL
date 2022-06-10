import socket
from _thread import *
from threading import Thread, Event
import pyaudio
import audioop
import math

class clientThread(Thread):
    def __init__(self, event, connection):
        Thread.__init__(self)
        self.stopped = event
        self.connection = connection
        self.client_id = 0

    def set_id(self, client_id):
        self.client_id = client_id

    def run(self):
        FORMAT = pyaudio.paInt16
        CHUNK = 1024
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        while not self.stopped.wait(1):

            data = stream.read(CHUNK, exception_on_overflow = False)

            rms = audioop.rms(data, 2)
            max_out = 10 * math.log10(rms + 1)



            message = str(self.client_id) + ":" + str(max_out)
            self.connection.send(str.encode(message))
        self.connection.send(str.encode('stop'))
        stream.stop_stream()
        stream.close()
        p.terminate()


clientConnection = socket.socket()
host = '192.168.55.160'
port = 5050

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
