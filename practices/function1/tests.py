'''
練習寫個函式 square
輸入: 1 個整數
回傳: 此整數的平方
'''
from unittest import TestCase
from .main import square

class Test(TestCase):
    def test_sample_input_1(self):
        self.assertEqual(square(2), 4)

    def test_sample_input_2(self):
        self.assertEqual(square(4), 16)
