#

import unittest
from src.homework.j_classes.class_a import Die



class TestDie(unittest.TestCase):

    def test_roll(self):
        die = Die()
        for _ in range(3):
            die.roll()
            roll_value = die.get_rolled_value()
            self.assertIn(roll_value, range(1, 7), "Roll value should be between 1 and 6")



        
unittest.main()