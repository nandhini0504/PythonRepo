import unittest
from src.calendarmodule_7.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualinput = weekday(8,26,2023)
        expectedoutput = "SATURDAY"
        self.assertEqual(actualinput, expectedoutput)



if __name__ == '__main__':
    unittest.main()