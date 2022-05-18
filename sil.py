import pyaudio

from array import array
from  math import log10
import audioop




FORMAT = pyaudio.paInt16
CHUNK = 1024
CHANNELS = 1
RATE = 44100
#RECORD_SECONDS = 5


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)





#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
while True:
    data = stream.read(CHUNK)
    data_chunk = array('h', stream.read(CHUNK))
    rms = audioop.rms(data,2)
    max_out = 10* log10(rms)
    print(max_out)










