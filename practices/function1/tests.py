'''
回答以下問題
'''
from unittest import TestCase


class Test(TestCase):
    def test_case_string_1(self):
        if '':
            a = 1
        else:
            a = 2
        self.assertEqual(a, )

    def test_case_string_2(self):
        if 'False':
            a = 1
        else:
            a = 2
        self.assertEqual(a, )

    def test_case_list_1(self):
        if []:
            a = 1
        else:
            a = 2
        self.assertEqual(a, )

    def test_case_list_2(self):
        if [False]:
            a = 1
        else:
            a = 2
        self.assertEqual(a, )

    def test_case_dict_1(self):
        if {}:
            a = 1
        else:
            a = 2
        self.assertEqual(a, )

    def test_case_dict_2(self):
        if {False, False}:
            a = 1
        else:
            a = 2
        self.assertEqual(a, )

    def test_case_bool_1(self):
        if False:
            a = 1
        else:
            a = 2
        self.assertEqual(a, )

    def test_case_dict_2(self):
        if True:
            a = 1
        else:
            a = 2
        self.assertEqual(a, )
