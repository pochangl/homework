'''
練習寫個會產生 IndentError 的程式碼
'''
from unittest import TestCase
class Test(TestCase):
    def test_case_1(self):
        try:
            from . import main
        except TypeError:
            pass
        else:
            self.fail('沒有出現 TypeError')