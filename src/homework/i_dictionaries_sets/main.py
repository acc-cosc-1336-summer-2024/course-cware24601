from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix


def main():
    while True:
        print("1-Get p distance matrix")
        print("2-Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            dna_list = []
            num_dna_list = int(input("Enter the number of sequences:"))

            for i in range (num_dna_list):
                list = input(f"Enter sequence {i+1}: ").split()
                dna_list.append(list)
            result = get_p_distance_matrix(dna_list)
            print("P Distance Matrix:")
            for row in result:
                print(row)
        
        elif choice == '2':
            break

        else:
            print("Invalid option. Please try again.")


        
main()