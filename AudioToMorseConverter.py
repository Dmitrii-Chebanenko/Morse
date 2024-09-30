import util
import math


class AudioToMorseConverter:
    def __init__(self, dot_len, dash_len, char_pause, let_pause, word_pause):
        self.__dot_len = dot_len
        self.__dash_len = dash_len
        self.__char_pause = char_pause
        self.__let_pause = let_pause
        self.__word_pause = word_pause

    def signal_to_morse(self, data, sample_rate):
        s = ''
        for word in util.split_arr_zeros(data.tolist(), int(self.__word_pause * sample_rate)):
            w = ''
            for let in util.split_arr_zeros(word, int(self.__let_pause * sample_rate)):
                l = ''
                for char in util.split_arr_zeros(let, int(self.__char_pause * sample_rate)):
                    ch = ''
                    if math.isclose(len(char), int(self.__dot_len * sample_rate), abs_tol=2):
                        ch = '.'
                    elif math.isclose(len(char), int(self.__dash_len * sample_rate), abs_tol=2):
                        ch = '-'
                    l += ch
                w+=l
                w+=' '
            if w!='':
                s+=w
                s+='* '
        return s[:-3]