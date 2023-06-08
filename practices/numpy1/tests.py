'''
https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv

寫個函式 def list_mul(a, b)
使用 numpy 將 a b 的數字互乘
並回傳結果
'''
from unittest import TestCase
import numpy as np
from .main import list_mul

class Test(TestCase):
    def test_sample_input_1(self):
        result = list(list_mul([1, 2, 3], [3, 4, 6]))
        self.assertEqual(result, [3, 8, 18])
