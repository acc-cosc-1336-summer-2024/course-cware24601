#main program
from re import A
import strings

def create_string():
    lang = "Python" #create the string
    print(lang)


def access_characters_in_a_string():
    lang = "Python"
    print(lang[0])
    print(lang[5])


def cannot_change_string_characters():
    lang = "Python"

    lang[0] = 'P' #can't change characters in a string


def loop_string_w_while():
    lang = "Python"
    index = 0

    while(index < len(lang)):
        print(lang[index])
        index += 1 #statement that eventually stops the loop


def loop_string_w_for():#function header
    lang = "Python"

    for i in range(0, len(lang)):
        print(lang[i])

def loop_strings_for_range():
    lang = "Python"

    for ch in lang:
        print(ch)
    

def get_hammering_distance(dna1, dna2):

    if len(dna1) != len(dna2):
        raise ValueError("DNA strands must be of equal length")
    
    return sum(1 for x, y in zip(dna1, dna2) if x != y)

def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[nuc] for nuc in dna[::-1])