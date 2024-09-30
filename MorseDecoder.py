from util import find_key_by_value
class MorseDecoder:
    def __init__(self, morse):
        self.__morse__ = morse

    def decode_msg(self, msg : str) -> str:
          ans = ''
          for word in msg.split(' * '):
              for let in word.split():
                  ans+= find_key_by_value(self.__morse__, let)
              ans+=' '
          return ans[:-1]