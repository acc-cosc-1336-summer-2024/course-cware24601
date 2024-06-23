from numbers import Rational


import unittest
from unittest import result

from src.homework.c_decisions.decisions import get_faculty_rating, get_options_ratio

class Test_Config(unittest.TestCase):

    def test_get_options_ratio(self):
        self.assertEqual(get_options_ratio, 5, 10)
    
    def test_get_options_ratio(self):
        self.assertEqual(result, get_options_ratio, 10, 20)
        
        
    def test_get_faculty__rating(self):
        self.assertEqual('Excellent', get_faculty_rating(.91))
        self.assertEqual('Very Good', get_faculty_rating(.85))
        self.assertEqual('Good', get_faculty_rating(.71))
        self.assertEqual('Needs Improvement', get_faculty_rating(.66))
        self.assertEqual('Unacceptable', get_faculty_rating(.45))
