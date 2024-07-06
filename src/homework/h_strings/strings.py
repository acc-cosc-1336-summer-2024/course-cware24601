def get_hamming_distance(dna1, dna2):

    distance = 0

    for i in range(len(dna1)):
            return "DNA are not equal" 

    if dna1[i] != dna2[i]:
            distance += 1

    return distance

def get_dna_complement(dna):
       complement = {'A': 'T' , 'T': 'A', 'C': 'G', 'G': 'C'}
       reversed_dna = dna[::-1]

       reverse_complement = '' .join(complement[nuc] for nuc in reversed_dna)

       return reverse_complement
    
