from MorseCoder import MorseCoder
from MorseToAudioConverter import MorseToAudioConverter
import sounddevice as sd

def CoderAudioExample(msg: str, dot_len, dash_len, freq, char_pause, let_pause, word_pause, sample_rate, amplitude):
    morse_to_audio_converter = MorseToAudioConverter(dot_len, dash_len, freq, char_pause, let_pause, word_pause,
                                                     sample_rate, amplitude)
    coded_msg = MorseCoder.code_eng_msg(msg)
    audio = morse_to_audio_converter.morse_to_signal(coded_msg)

    sd.play(audio, sample_rate)
    sd.wait()

if __name__ == '__main__':
    msg = "sos me"
    dot_len = 0.1
    dash_len = 0.3
    freq = 16000
    char_pause = 0.1
    let_pause = char_pause * 3
    word_pause = char_pause * 7
    sample_rate = 2048
    amplitude = 0.5
    CoderAudioExample(msg, dot_len, dash_len, freq, char_pause, let_pause, word_pause, sample_rate, amplitude)