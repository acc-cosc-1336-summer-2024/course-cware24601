#main program
import strings

#strings.create_string()
#strings.access_characters_in_a_string()
#stings.cannot_change_string_characters()
#strings.loop_string_w_while()
strings.loop_string_w_for()
strings.loop_strings_for_range()

import math

def get_factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * get(num-1)
    
def sum_odd_numbers(num):
    return sum(i for i in range(1, num+1, 2))

def main():
    while True:
        print("Homework 3 Menu")
        print("1-Factorial")
        print("2-Sum Odd Numbers")
        print("3-Exit")

        user = int(input("Choose an option"))

        if user == 1:
            while True:
                num = int(input("Enter a number (0 < number < 10):"))
                if 0 < num < 10:
                    break
                    
                    print("Invalid input. Please try again.")
                result = factorial(num)
                print(f"The factorial of {num is {result}}")


        elif user == 2:
            while True:
                num = in(input("Enter a number(0 < number < 100)"):
                         
                         if 0 < num < 100
                            break
                        print("Invalid input. Please try again.")
                    result = sum_odd_numbers(num)
                    print(f"The sum of odd numbers to {num} is {result}")


                elif user == 3:
                exit_confirm = input("Are you sure you want to exit? (yes/no): ")

                if exit_confirm.lower() == 'yes':
                break
                
                continue_confirm = input("Do you want to continue using the menu? (yes/no) ")
                if continue_confirm.lower() != 'yes':
                break
