'''
練習寫個函式 absolute
輸入: 1 個整數
回傳: 此整數絕對值
'''
from unittest import TestCase
from .main import minus

class Test(TestCase):
    def test_case_1(self):
        result = minus(1, 2)
        self.assertEqual(result, -1)

    def test_case_2(self):
        result = minus(a=1, b=2)
        self.assertEqual(result, -1)

    def test_case_3(self):
        result = minus(b=2, a=1)
        self.assertEqual(result, -1)

    def test_case_4(self):
        result = minus(2, a=1)
        self.assertEqual(result, -1)