import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix



class test_config(unittest.TestCase):
    def test_p_distance(self):
        list1 = ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        list2 = ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
        expected_result = 0.4
        result = get_p_distance(list1, list2)
        self.assertAlmostEqual(result, expected_result, places=5)



    def test_get_p_distance_matrix(self):
        dna_strings = [

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

        result = get_p_distance_matrix(dna_strings)
        for i in range(len(expected_result)):
            for j in range(len(expected_result[i])):
                self.assertAlmostEqual(result[i][j], expected_result[i][j], places=5)




                unittest.main()