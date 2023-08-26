import unittest
from src.percentage_3.utils import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualinput = percentage_calculation({'Krishna': [67,68,69], 'Arjun': [70,98,63],'Malika': [52,56,60]}, 'Malika')
        expectedoutput = 56
        self.assertEqual(actualinput, format(expectedoutput,'.2f'))  # add assertion here

    def test_something1(self):
        actualinput = percentage_calculation({'Harsh': [25,26.5,28], 'Anurag': [26,28,30]}, 'Harsh')
        expectedoutput = 26.50
        self.assertEqual(actualinput, format(expectedoutput,'.2f'))  # add assertion here


if __name__ == '__main__':
    unittest.main()