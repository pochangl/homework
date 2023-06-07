'''
練習寫個函式 absolute
輸入: 1 個整數
回傳: 此整數絕對值
'''
from unittest import TestCase
from .main import absolute

class Test(TestCase):
    def test_sample_input_1(self):
        self.assertEqual(absolute(2), 2)

    def test_sample_input_2(self):
        self.assertEqual(absolute(-4), 4)
