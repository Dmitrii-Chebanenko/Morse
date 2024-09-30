import numpy as np

class MorseToAudioConverter:
    def __init__(self, dot_len, dash_len, freq, char_pause, let_pause, word_pause, sample_rate, amplitude):
        self.__dot_len = dot_len
        self.__dash_len = dash_len
        self.__freq = freq
        self.__char_pause = char_pause
        self.__let_pause = let_pause
        self.__word_pause = word_pause
        self.__sample_rate = sample_rate
        self.__amplitude = amplitude

    def morse_to_signal(self, msg : str):
        signals = []
        for word in msg.split('*'):
            for letter in word.split():
                for char in letter:
                    signals.append(self.gen_audio_sym(char))
                    signals.append(self.gen_silent(self.__char_pause))
                signals.append(self.gen_silent(self.__let_pause - self.__char_pause))
            signals.append(self.gen_silent(self.__word_pause - self.__let_pause))
        return np.concatenate(signals)

    def gen_audio_sym(self, sym : str):
        if sym == '-':
            t = np.linspace(0, self.__dash_len, int(self.__dash_len * self.__sample_rate))
            return self.__amplitude * np.sin(2 * np.pi * self.__freq * t)
        elif sym == '.':
            t = np.linspace(0, self.__dot_len, int(self.__dot_len * self.__sample_rate))
            return self.__amplitude * np.sin(2 * np.pi * self.__freq * t)

    def gen_silent(self, duration):
            return np.zeros(int(self.__sample_rate * duration))