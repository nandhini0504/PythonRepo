import unittest
import numpy as np
from src.min_max_9.utils import minimum

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_array=([[2,5],[3,7],[1,3],[4,0]],int)
        actualoutput=minimum(test_array)
        expectedoutput=3
        self.assertEqual(actualoutput,expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()