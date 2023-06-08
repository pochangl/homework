'''
練習使用 map 將字串轉成數字 list
'''
from unittest import TestCase
from .main import str_to_list

class Test(TestCase):
    def test_sample_input_1(self):
        values = list(str_to_list('1 2 3'))
        self.assertEqual(values, [1, 2, 3])

    def test_sample_input_2(self):
        values = list(str_to_list('2 3 4'))
        self.assertEqual(values, [2, 3, 4])
