'''
猜幾個參數
'''
from unittest import TestCase
from .main import args_length

class Test(TestCase):
    def test_case_1(self):
        result = args_length(1, 2)
        self.assertEqual(result, )

    def test_case_2(self):
        result = args_length(1, 2, 3, 4)
        self.assertEqual(result, )

    def test_case_3(self):
        result = args_length((1, 2), 2)
        self.assertEqual(result, )

    def test_case_4(self):
        result = args_length(a=1, b=2)
        self.assertEqual(result, )

    def test_case_5(self):
        result = args_length(a=(1, 2), b=2)
        self.assertEqual(result, )
