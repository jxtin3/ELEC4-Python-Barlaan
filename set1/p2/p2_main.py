# p2_main.py - Main program using student_utils module
# Name: Justine Barlaan
# Section: IV-BSIT B
# Activity Code: P2
# Date: November 18, 2026

# Import 1: import module_name
# Brings in the whole toolbox; call functions using module_name.function()
import student_utils

# Import 2: date and time
from datetime import datetime

# Function 1 to get one valid grade (0-100)
def get_valid_grade(validgrade):
    while True:
        grade = input(validgrade)
        try:
            grade = float(grade)
            if grade < 0 or grade > 100:
                print("Error: Grade must be between 0 and 100.")
            else:
                return grade
        except:
            print("Error: Please enter a number.")

# Function 2- get all grades
def get_grades():
    while True:
        count = input("How many grades? ")
        try:
            count = int(count)
            if count > 0:
                break
            print("Error: Enter a positive number.")
        except:
            print("Error: Enter a valid integer.")

    grades = []
    i = 1
    while i <= count:
        grade = get_valid_grade("Enter grade " + str(i) + ": ")
        grades.append(grade)
        i = i + 1
    return grades

# Function 3 to display results
def display_results(grades):
    if len(grades) == 0:
        print("No grades yet.")
        return

    avg = student_utils.compute_average(grades)
    high = student_utils.get_highest(grades)
    low = student_utils.get_lowest(grades)
    status = student_utils.get_pass_fail(grades)

    print("\n=== GRADE REPORT ===")
    print("Grades: " + str(grades))
    print("Count: " + str(len(grades)))
    print("Average: " + str(round(avg, 2)))
    print("Highest: " + str(high))
    print("Lowest: " + str(low))
    print("Status: " + status)
    print("=====================\n")


# Main program
grades = []

while True:
    print("\n=== STUDENT GRADE CALCULATOR ===")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")
    print("================================")

    choice = input("Choose (1-3): ")

    if choice == "1":
        grades = get_grades()
        print("Grades saved!")
    elif choice == "2":
        display_results(grades)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

# Report timestamp (uses built-in datetime module)
now = datetime.now()
print("\nReport generated on: " + str(now))