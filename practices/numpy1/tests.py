'''
https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv
使用 pandas 從以上 csv 取得平均年齡
並存入變數 average_age
'''
from unittest import TestCase
from .main import average_age

class Test(TestCase):
    def test_sample_input_1(self):
        self.assertEqual(average_age, 104/3)
