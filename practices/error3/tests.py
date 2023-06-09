'''
練習寫個會產生 SyntaxError 的程式碼
'''
from unittest import TestCase
class Test(TestCase):
    def test_case_1(self):
        try:
            from . import main
        except SyntaxError:
            pass
        except Exception as error:
            self.fail(f'{type(error)} 不是 SyntaxError')
        else:
            self.fail('沒有出現 SyntaxError')