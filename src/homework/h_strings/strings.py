import unittest


def get_hamming_distance(dna1, dna2):
    if len(dna1 ) != len(dna2):
        raise ValueError("Strands must be of equal length.")
    
    get_hamming_distance = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            get_hamming_distance += 1


        return get_hamming_distance

    
def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented_dna = ''.join(complement[base]for base in dna)

    reverse_complement = complemented_dna[::-1]
    return reverse_complement
    
