import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix



class test_config(unittest.TestCase):

    def test_p_distance(self):
        self.assertAlmostEqual(get_p_distance(
        list1 = ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        list2 = ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
        ), 0.4, places=5)


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

        result = get_p_distance_matrix(dna_lists)
        
        for row_exp, row_res in zip(expected_result, result):

            for val_exp, val_res in zip(row_exp, row_res):
                self.assertAlmostEqual(val_exp, val_res, places=5)



unittest.main()