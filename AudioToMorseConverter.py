import math


class AudioToMorseConverter:
    def __init__(self, dot_len, dash_len, char_pause, let_pause, word_pause):
        self.__dot_len = dot_len
        self.__dash_len = dash_len
        self.__char_pause = char_pause
        self.__let_pause = let_pause
        self.__word_pause = word_pause
        self.__tmp_line_len = 0
        self.__zeros_line_len = 0

    def signal_to_morse(self, data, sample_rate):
        msg = ""
        for i in data:

            if i != 0:
                self.__tmp_line_len += 1
                if math.isclose(self.__zeros_line_len, int(sample_rate * self.__word_pause), abs_tol=2):
                    msg += ' * '
                    self.__zeros_line_len = 0
                elif math.isclose(self.__zeros_line_len, int(sample_rate * self.__let_pause), abs_tol=2):
                    msg += ' '
                    self.__zeros_line_len = 0
                elif math.isclose(self.__zeros_line_len, int(sample_rate * self.__char_pause), abs_tol=2):
                    self.__zeros_line_len = 0
            else:
                self.__zeros_line_len += 1
                if math.isclose(self.__tmp_line_len, int(sample_rate * self.__dash_len), abs_tol=2):
                    msg += '-'
                    self.__tmp_line_len = 0
                elif math.isclose(self.__tmp_line_len, int(sample_rate * self.__dot_len), abs_tol=2):
                    msg += '.'
                    self.__tmp_line_len = 0

        return msg
