#main program
from unittest.main import main
import strings

#strings.create_string()
#strings.access_characters_in_a_string()
#stings.cannot_change_string_characters()
#strings.loop_string_w_while()


import math
def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        return "Strings are not equal length"
    return sum(c1 != c2 for c1, c2 in zip(dna1, dna2))

def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna[::-1])


def display_menu():
    while True:
        print(' Menu')
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            str1 = input("Enter the first DNA string: ")
            str2 = input("Enter the second DNA string: ")
            result = strings.get_hamming_distance(str1, str2)
            print("Hamming Distance: ", result)

        elif choice == '2':
            dna = input("Enter the first DNA string: ")
            result = strings.get_dna_complement(dna)
            
            print("DNA Complement: ", result)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please 1, 2, or 3.")

    if __name__ == "__main__":
        main()