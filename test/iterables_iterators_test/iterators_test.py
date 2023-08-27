import unittest
from src.Iterables_14.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        N=4
        test_list=['a','a','c','d']
        K=2
        actualoutput=itertools_func(N,test_list,K)
        expectedoutput=0.833
        self.assertEqual(actualoutput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()