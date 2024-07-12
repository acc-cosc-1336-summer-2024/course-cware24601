def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The DNA strings must be equal length.")
    
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    return differences / len(list1)

def get_p_distance_matrix(dna_lists):
   result = []
   for list1 in dna_lists:
       row = []
       for list2 in dna_lists:
           row.append(get_p_distance(list1, list2))
           result.append(row)
       return result