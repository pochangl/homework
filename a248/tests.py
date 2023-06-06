from unittest import TestCase
from utils import mock_stdin, mock_stdout

sample_input_1 ='''
18467 41 10
26500 6334 10
15724 19169 10
10 5 3
'''.strip()

sample_output_1 = '''
450.4146341463
4.1837701294
0.8202827481
2.000
'''.split()

class TestA248(TestCase):
    def test_sample_input_1(self):
        with mock_stdin(sample_input_1), mock_stdout() as stdout:
            from . import main
        self.assertEqual(stdout.read(), sample_output_1)
