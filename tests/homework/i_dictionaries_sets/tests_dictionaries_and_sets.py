import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix



class test_config(unittest.TestCase):

    def test_p_distance(self):
        self.assertAlmostEqual(get_p_distance(
        ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
        ), 0.4)


    def test_get_p_distance_matrix(self): 
        dna_lists = [

            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
            ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],
            ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']

        ]
        expected_result = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2]
            [0.1, 0.3, 0.2, 0.0]
        ]

        self.assertEqual(get_p_distance_matrix(dna_lists),
expected_result)


unittest.main()