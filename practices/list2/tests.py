'''
練習寫個函式 range_as_list
輸入: 1 個整數 n
回傳: [0, 1, 2, ....., n]
'''
from unittest import TestCase
from .main import concat_list

class Test(TestCase):
    def test_sample_input_1(self):
        self.assertEqual(concat_list([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_sample_input_2(self):
        self.assertEqual(concat_list([1], [9]), [1, 9])
