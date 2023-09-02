import unittest

from src.linear_algebra_10.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        list1 =[[1,3],[2,4]]
        actualinput =linear_algebra(list1)
        expectedoutput=-2.0
        self.assertEqual(actualinput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()