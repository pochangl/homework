'''
練習寫個函式 get_sum
輸入: 1 個全是整數的 list
回傳: 輸入的所有值加總

內建函式 https://docs.python.org/3/library/functions.html
'''
from unittest import TestCase
from .main import get_sum

class Test(TestCase):
    def test_sample_input_1(self):
        self.assertEqual(get_sum([1, 2]), 3)

    def test_sample_input_2(self):
        self.assertEqual(get_sum([1, 2, 4]), 7)
