from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix


def display_menu():
    print("Menu:")
    print("1. Get p distance matrix")
    print ("2. Exit")


def get_choice():
    return input('Enter your choice (1/2): ')


def handle_choice(choice):
    
    if choice == '1':
        dna_strings = input('Enter DNA sequences separated by newlines').strip().split('\n')
        dna_lists = [list(dna.strip()) for dna in a dna_strings if dna.strip()]
        result = get_p_distance_matrix(dna_lists)
        print('p Distance Matrix:')