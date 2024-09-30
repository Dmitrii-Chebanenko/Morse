import globals
class MorseCoder:
    @staticmethod
    def code_eng_msg(msg : str) -> str:
          msg = msg.upper()
          ans = ''
          for i in msg:
              ans+=globals.eng_morse_dict[i]
              ans+=' '
          return ans
