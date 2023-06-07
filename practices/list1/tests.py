'''
練習寫個函式 range_as_list
輸入: 1 個整數 n
回傳: [0, 1, 2, ....., n]
'''
from unittest import TestCase
from .main import range_as_list

class Test(TestCase):
    def test_sample_input_1(self):
        self.assertEqual(list(range_as_list(4)), [0, 1, 2, 3])

    def test_sample_input_2(self):
        self.assertEqual(list(range_as_list(5)), [0, 1, 2, 3, 4])
