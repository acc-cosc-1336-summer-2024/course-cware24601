import unittest

from src.examples.h_strings.strings import test_config
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):
    

    def test_get_hamming_distance(self):

        distance = get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        self.assertEqual(distance, 7)
        print(distance)

    def test_dna_complement(self):
        complement = get_dna_complement("AAAACCCGGT")
        self.assertEqual(complement, "ACCGGGTTTT")
        
        print(complement)

if __name__ == '__main__':
    unittest.main()