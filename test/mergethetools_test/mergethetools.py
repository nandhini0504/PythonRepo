import unittest
from src.mergethetools_6.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_string="AABCAAADA"
        k=3
        actualoutput=merge_the_tools(test_string, k)
        expectedoutput=['AB','CA','AD']
        self.assertEqual(actualoutput,expectedoutput)  # testcase1


if __name__ == '__main__':
    unittest.main()