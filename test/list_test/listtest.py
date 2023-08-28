import unittest #This line imports the unittest module, which provides tools for testing code.
from src.list_2.driver import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = ['insert 0 5', 'insert 1 10', 'append 15', 'sort', 'remove 10', 'reverse', 'pop', 'print']
        actualinput= list_new(x)
        expectedoutput=[15]
        self.assertEqual(actualinput,expectedoutput) # use self.assertEqual() to check if the actual output matches the expected output.
if __name__ == '__main__':
    unittest.main()