import numpy as np

from MorseCoder import MorseCoder
from MorseToAudioConverter import MorseToAudioConverter
from scipy.io.wavfile import write
import sounddevice as sd


if __name__ == '__main__':
    a = MorseCoder.code_eng_msg("sosi eblan")
    dot_len = 0.1
    dash_len = 0.3
    freq = 16000
    char_pause = 0.1
    let_pause = char_pause * 3
    word_pause = char_pause * 7
    sample_rate = 2048
    amplitude = 0.5
    morse_to_audio_converter = MorseToAudioConverter(dot_len, dash_len, freq, char_pause, let_pause, word_pause,
                                                     sample_rate, amplitude)

    audio = morse_to_audio_converter.morse_to_signal(a)

    write('morse_code.wav', sample_rate, audio.astype(np.float32))

    sd.play(audio, sample_rate)
    sd.wait()