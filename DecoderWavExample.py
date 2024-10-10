import globals

from scipy.io.wavfile import read
from AudioToMorseConverter import AudioToMorseConverter
from MorseDecoder import MorseDecoder


def DecoderWavExample(data, sampling_rate, dot_len, dash_len, char_pause, let_pause, word_pause):
    con = AudioToMorseConverter(dot_len, dash_len, char_pause, let_pause, word_pause)
    code_msg = con.signal_to_morse(data, sampling_rate)
    print(code_msg)
    m_d = MorseDecoder(globals.eng_morse_dict)
    msg = m_d.decode_msg(code_msg)
    print(msg)


if __name__ == '__main__':
    dot_len = 0.1
    dash_len = 0.3
    char_pause = 0.1
    let_pause = char_pause * 3
    word_pause = char_pause * 7
    sampling_rate, data = read('morse_code.wav')
    DecoderWavExample(data, sampling_rate, dot_len, dash_len, char_pause, let_pause, word_pause)
