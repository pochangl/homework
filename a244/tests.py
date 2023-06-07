from unittest import TestCase
from utils import mock_stdin, mock_stdout, rerun_module

sample_input_1 ='''
4
1 2 3
2 2 3
3 2 3
4 2 3'''

sample_output_1 = '''
5
-1
6
0
'''


class Test(TestCase):
    def test_sample_input_1(self):
        with mock_stdin(sample_input_1.strip()), mock_stdout() as stdout:
            rerun_module('a244.main')
        self.assertEqual(stdout.read().strip(), sample_output_1.strip())
