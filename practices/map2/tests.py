'''
寫一個函數 square_all
輸入: 1 組只有 整數的 list
輸出: 把輸入所有的數字變成平方
練習使用 map 將 list 裡的數字做平方
'''
from unittest import TestCase
from .main import square_all

class Test(TestCase):
    def test_sample_input_1(self):
        values = list(square_all([1, 2, 3]))
        self.assertEqual(values, [1, 4, 9])

    def test_sample_input_2(self):
        values = list(square_all([5, 6]))
        self.assertEqual(values, [25, 36])
