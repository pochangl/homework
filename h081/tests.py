from unittest import TestCase
from utils import mock_stdin, mock_stdout, rerun_module

sample_input_1 ='''
3 10
50 20 45'''

sample_output_1 = '0'

sample_input_2 = '''
6 10
30 20 45 38 10 20'''

sample_output_2 = '25'

class Test(TestCase):
    def test_sample_input_1(self):
        with mock_stdin(sample_input_1.strip()), mock_stdout() as stdout:
            rerun_module('h081.main')
        self.assertEqual(stdout.read().strip(), sample_output_1.strip())

    def test_sample_input_2(self):
        with mock_stdin(sample_input_2.strip()), mock_stdout() as stdout:
            rerun_module('h081.main')
        self.assertEqual(stdout.read().strip(), sample_output_2.strip())
