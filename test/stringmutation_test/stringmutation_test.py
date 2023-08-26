import unittest
from src.string_mutation_5.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualoutput= mutate_string("WELCME",4,"O")
        expectedoutput="WELCOME"

        self.assertEqual(actualoutput,expectedoutput)  # add assertion here
    def test_something(self):
        actualoutput= mutate_string("SMMER",1,"U")
        expectedoutput="SUMMER"

        self.assertEqual(actualoutput,expectedoutput)  # add assertion here

if __name__ == '__main__':
    unittest.main()