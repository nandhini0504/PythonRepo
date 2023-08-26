from src.secondmax_num_4.utils import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expectedOutput = second_max_number(5, [2,3,6,7,5])
        actualOutput = 6
        self.assertEqual(expectedOutput, actualOutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()