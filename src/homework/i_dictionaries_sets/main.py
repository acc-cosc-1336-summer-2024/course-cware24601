def get_p_distance_matrix(sequences):

    matrix = []
    for i in range(len(sequences)):
        row = []
        for j in range(len(sequences)):
            if i == j:
                row.append(0.0)
            else:
                distance = sum(1 for a, b in zip(sequences[i], sequences[j]) if a != b) / len(sequences[i])
                row.append(distance)
        matrix.append(row)
    return matrix

def display_menu():
    print("1-Get p distance matrix")
    print("2-Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sequences = input("Enter a list of sequences separated by spaces: ").split()
            matrix = get_p_distance_matrix(sequences)
            print("P-distance matrix:")
            for row in matrix:
                print(" ".join(map(str, row)))
        elif choice == '2':
            print("Exiting the program.")
            
        else:
            print("Invalid choice. Please try again.")


    main()