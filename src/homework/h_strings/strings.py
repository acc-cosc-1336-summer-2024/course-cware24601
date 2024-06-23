#main program
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
    