# p4_exceptions.py - Safe Menu Program
# Name: Justine Barlaan
# Section: IV-BSIT B
# Activity Code: P4
# Date: November 19, 2026


def display_menu():
    print("\n=== SAFE MENU PROGRAM ===")
    print("1. Divide two numbers")
    print("2. Open a file")
    print("3. Exit")
    print("=========================")


def divide_numbers():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        result = first / second
    except ValueError:
        # The user typed letters instead of a number
        print("Error: Please enter numbers only.")
    except ZeroDivisionError:
        # The second number was 0
        print("Error: You cannot divide by zero.")
    else:
        # Runs only if there was no error
        print("Result:", result)
    finally:
        # Runs every time, with or without an error
        print("Division finished.")


def open_file():
    file_name = input("Enter the file name: ")
    try:
        file = open(file_name, "r")
        contents = file.read()
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("=== File contents ===")
        print(contents)
    finally:
        print("File operation finished.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
