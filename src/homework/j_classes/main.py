
from class_a import Die


def main():
    die = Die()
    while True:
        print("\nMenu:")
        print("1. Roll the die")
        print("2. Exit")
        choice = input("Enter your choice: ")


        if choice == '1':
            die.roll()
            print(die)

        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()