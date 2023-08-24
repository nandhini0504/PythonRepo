from second_max_number.core.utils import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expectedOutput = second_max_number(5, [1,23,45,32,3])
        actualOutput = 32
        self.assertEqual(expectedOutput, actualOutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()