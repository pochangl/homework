from unittest import TestCase
from utils import mock_stdin, mock_stdout

sample_input_1 ='''
3 10
50 20 45''' * 10000

sample_output_1 = '''
6 10
30 20 45 38 10 20''' * 10000

class Test(TestCase):
    def test_sample_input_1(self):
        with mock_stdin(sample_input_1.strip()), mock_stdout() as stdout:
            from . import main
        self.assertEqual(stdout.read().strip(), sample_output_1.strip())
