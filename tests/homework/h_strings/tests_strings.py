import unittest
from unittest.main import main

from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):
    

    def test_get_hamming_distance(self):

        result = get_hamming_distance(self)
        dna1 = 'GAGCCTACTAACGGGAT'
        dna2 = 'CATCGTAATGACGGCCT'
        expected_result = 7
        self.assertEqual(result, expected_result)
        print(result)

    def test_dna_complement(self):
        dna = 'AAAACCCGGT'
        expected_result = 'ACCGGGTTTT'
        result = get_dna_complement(dna)
        self.assertEqual(result, expected_result)

        print (result)

        

main()

    