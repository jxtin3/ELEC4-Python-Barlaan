# Student Grade Calculator - P1
# Name: Justine Barlaan
# Section: IV-BSIT B
# Activity Code: P1
# Date: November 17, 2026

# Function 1 to get one valid grade (0-100)
def get_valid_grade(validgrade):
    # while true=it repeat forever until someone stop it
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

        #Same Logic, Different Keywords(except)


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
    #create empty list
    i = 1
    while i <= count:
        grade = get_valid_grade("Enter grade " + str(i) + ": ")
        grades.append(grade)
        # Increment the counter
        i = i + 1
    return grades


# Function 3 to compute average
def compute_average(grades):
    if len(grades) == 0:
        return 0
    total = 0
    for g in grades:
        total = total + g
    return total / len(grades)
    # Divide by count of grades


# Function 4 to get highest grade
def get_highest(grades):
    if len(grades) == 0:
        return 0
    highest = grades[0]
    for g in grades:
        if g > highest:
            highest = g
    return highest
    


# Function 5 - lowest grade
def get_lowest(grades):
    if len(grades) == 0:
        return 0
    lowest = grades[0]
    for g in grades:
        if g < lowest:
            lowest = g
    return lowest


# Function 6 - get pass/fail status
def get_pass_fail(grades):
    avg = compute_average(grades)
    if avg >= 75:
        return "PASS"
    else:
        return "FAIL"


# Function 7 to display results
def display_results(grades):
    if len(grades) == 0:
        print("No grades yet.")
        return

    avg = compute_average(grades)
    high = get_highest(grades)
    low = get_lowest(grades)
    status = get_pass_fail(grades)

    print("\n--- GRADE REPORT ---")
    print("Grades: " + str(grades))
    print("Count: " + str(len(grades)))
    print("Average: " + str(round(avg, 2)))
    print("Highest: " + str(high))
    print("Lowest: " + str(low))
    print("Status: " + status)
    print("--------------------\n")


# Function 8 to show menu
def show_menu():
    print("\n--- STUDENT GRADE CALCULATOR ---")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")
    print("--------------------------------")

# Main program
grades = []

while True:
    show_menu()
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


# Local vs Global Variables (Explanation)

# LOCAL VARIABLE = belongs to ONE place only
# GLOBAL VARIABLE = visible to EVERYWHERE


# IN THIS PROGRAM:

# 'grades' in the main loop is LOCAL to main:
#   grades = []               # Created here
#   grades = get_grades()     # Replaced here
#   display_results(grades)   # Passed to function here

# When main calls display_results(grades), the function receive it as a PARAMETER. 
# This creates a NEW local variable 'grades'inside display_results(). The same happens in
# compute_average(grades), get_highest(grades), etc.
#
# Each function has its OWN 'grades' variable. They don't share
# one variable - they each get a COPY of the reference.




# FUNCTION 1 FLOW==========================
# START
#   │
#   ▼
# while True:  <---------------------------------
#   │                                           │
#   ▼                                           │
# input(validgrade) == user types "abc"         │
#   │                                           │
#   ▼                                           │
# try: float("abc") == fail!                    │
#   │                                           │
#   ▼                                           |
# except: print error----------------------------
#   │
#   ▼
# while True: (back to top)
#   │
#   ▼
# input(prompt)  ── user types "150"
#   │
#   ▼
# try: float("150") → 150.0  
#   │
#   ▼
# if 0 <= 150 <= 100?  NO
#   │
#   ▼
# else: print "0-100 error"
#   │
#   ▼
# while True: (back to top)
#   │
#   ▼
# input(prompt)  ── user types "85"
#   │
#   ▼
# try: float("85") → 85.0  
#   │
#   ▼
# if 0 <= 85 <= 100?  YES
#   │
#   ▼
# return 85.0  ──► EXIT FUNCTION, send 85.0 back


# Function 2 FLOW =========================
# get_grades() called
#       │
#       ▼
# while True:
#       │
#       ▼
# input("How many grades? ") ── user types "abc"
#       │
#       ▼
# try: int("abc") - CRASH
#       │
#       ▼
# except: print "Enter valid integer"
#       │
#       ▼
# while True: (back to top)
#       │
#       ▼
# input("How many grades? ") - if user types "0"
#       │
#       ▼
# try: int("0") → 0
#       │
#       ▼
# if 0 > 0? NO
#       │
#       ▼
# print "Enter positive number"
#       │
#       ▼
# while True: (back to top)
#       │
#       ▼
# input("How many grades? ") - if user input "3"
#       │
#       ▼
# try: int("3") → 3
#       │
#       ▼
# if 3 > 0? YES → break  
#       │
#       ▼
# grades = []
# i = 1
# while i <= 3:
#       │
#       ▼
# i=1: get_valid_grade("Enter grade 1: ") → returns 85.0
#       grades.append(85.0)  → grades = [85.0]
#       i = 2
#       │
#       ▼
# i=2: get_valid_grade("Enter grade 2: ") → returns 90.0
#       grades.append(90.0)  → grades = [85.0, 90.0]
#       i = 3
#       │
#       ▼
# i=3: get_valid_grade("Enter grade 3: ") → returns 75.0
#       grades.append(75.0)  → grades = [85.0, 90.0, 75.0]
#       i = 4
#       │
#       ▼
# i=4: 4 <= 3? NO → exit loop
#       │
#       ▼
# return grades  → [85.0, 90.0, 75.0]


# Function 3 FLOW =========================
# total = 0

# Loop 1: g = 85.0
#   total = 0 + 85.0 = 85.0

# Loop 2: g = 90.0
#   total = 85.0 + 90.0 = 175.0

# Loop 3: g = 75.0
#   total = 175.0 + 75.0 = 250.0

# End of loop

# return 250.0 / 3 = 83.33...


# Function 4 FLOW =========================
# highest = grades[0] = 75.0

# Loop 1: g = 75.0
#   75.0 > 75.0? NO → highest stays 75.0

# Loop 2: g = 90.0
#   90.0 > 75.0? YES → highest = 90.0

# Loop 3: g = 85.0
#   85.0 > 90.0? NO → highest stays 90.0

# End of loop

# return 90.0

