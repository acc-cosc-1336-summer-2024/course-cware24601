#main program
from tkinter import Menu
import unittest
import strings



def menu():
    while True:
        print("Menu:")
        print("1. Hamming Distance")
        print("2. DNA Complement")
        print("3. Exit")

        choice = input('Enter your choice (1/2/3): ')


        if choice == '1':
            dna1 = input('Enter 1st DNA string: ')
            dna2 = input('Enter 2nd DNA string: ')        
            try:
               result = strings.get_hamming_distance(dna1, dna2)
               print('Hamming Distance:', result)

            except ValueError as e:
               print(e)

        elif choice == '2':
            dna = input('Enter DNA string: ')
            result = strings.get_dna_complement(dna)
            print('DNA Complement:', result)

        elif choice == '3':
            print('Exiting the program')

        else:
            print('Invalid choice. Enter 1, 2, or 3')





menu()
        
            