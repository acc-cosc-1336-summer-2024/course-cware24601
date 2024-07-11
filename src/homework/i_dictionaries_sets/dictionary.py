def get_p_distance(list1, list2):
    assert len(list1) == len(list2),
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    
    p_distance = differences / len(list1)

    return p_distance

def get_p_distance_matrix(lists):
    n = len(lists)
    p_distance_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                p_distance_matrix[i][j] = get_p_distance(list[i], lists[j])

            else:
                p_distance_matrix = 0.0

        return p_distance_matrix
    
    for row in p_distance_matrix:
        print(" ".join(f"{dist:.5f}" for dist in row))

        