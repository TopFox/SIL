import pyaudio
import wave
from array import array
from  math import log10

FORMAT = pyaudio.paInt16
CHUNK = 1024
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

p2 = pyaudio.PyAudio()
stream_lecture = p2.open(format=FORMAT,
                         channels=CHANNELS,
                         rate=RATE,
                         output=True)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    data_chunk = array('h', stream.read(CHUNK))
    max_out = 20* log10(max(data_chunk))
    print(max_out)
    #stream_lecture.write(data)

stream.stop_stream()
stream.close()
p.terminate()

stream_lecture.stop_stream()
stream_lecture.close()

p2.terminate()



