import pyaudio
import numpy as np
from DecoderWavExample import DecoderWavExample

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 2048
CHUNK = 1024

dot_len = 0.1
dash_len = 0.3
char_pause = 0.1
let_pause = char_pause * 3
word_pause = char_pause * 7

print("Начало записи... (нажмите Ctrl+C для остановки)")

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
try:
    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)
        DecoderWavExample(data, RATE, dot_len, dash_len, char_pause, let_pause, word_pause)


except KeyboardInterrupt:
    print("\nЗапись остановлена.")

finally:

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Аудиопоток закрыт.")
