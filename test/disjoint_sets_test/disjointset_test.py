import unittest
from src.disjoint_sets_15.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = [1, 2, 3, 4, 5]
        x = [1, 8, 9]
        y = [2, 3, 6]
        actualinput=disjoint(s,x,y)
        expectedoutput=-1.0
        self.assertEqual(actualinput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()