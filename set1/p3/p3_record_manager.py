# p3_record_manager.py - Student Record Manager
# Name: Justine Barlaan
# Section: IV-BSIT B
# Activity Code: P3
# Date: November 19, 2026

# Import: datetime for timestamp
from datetime import datetime

# student_names = LIST to keep order and allow indexing
# student_set = SET to check duplicates fast (case-insensitive)

student_names = []
student_set = set()


def display_menu():
    print("\n=== STUDENT RECORD MANAGER ===")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Display all students")
    print("5. Exit")
    print("==============================")


def normalize_name(name):
    """Convert to lowercase for case-insensitive comparison."""
    return name.strip().lower()


def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    norm = normalize_name(name)
    if norm in student_set:
        print("Error: Student already exists.")
        return

    student_names.append(name)
    student_set.add(norm)
    print("Student added.")


def remove_student():
    name = input("Enter student name to remove: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    norm = normalize_name(name)
    if norm not in student_set:
        print("Error: Student not found.")
        return

    # Find and remove the original case name
    for i, n in enumerate(student_names):
        if normalize_name(n) == norm:
            student_names.pop(i)
            break

    student_set.remove(norm)
    print("Student removed.")


def search_student():
    query = input("Enter name to search: ").strip().lower()
    if not query:
        print("Error: Search cannot be empty.")
        return

    found = []
    for n in student_names:
        if query in n.lower():
            found.append(n)

    if not found:
        print("No matching students.")
        return

    print("\n=== SEARCH RESULTS ===")
    for i, n in enumerate(found, 1):
        print(str(i) + ". " + n)
    print("======================")


def display_all():
    if not student_names:
        print("No students yet.")
        return

    sorted_names = sorted(student_names, key=lambda x: x.lower())
    print("\n=== ALL STUDENTS ===")
    for i, n in enumerate(sorted_names, 1):
        print(str(i) + ". " + n)
    print("Total: " + str(len(student_names)))
    print("====================")


def main():
    while True:
        display_menu()
        choice = input("Choose (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

    # Timestamp
    now = datetime.now()
    print("\nProgram ended on: " + str(now))


# Run program
main()

# List vs Set Explanation

# LIST = ordered collection, allows duplicates
#   student_names = []  

#       We use LIST to:
#     - Keep insertion order
#     - Allow numbering (1., 2., 3.)
#     - Sort alphabetically for display
#     - Search with partial match (loop through)

# SET = unordered collection, NO duplicates allowed
#   student_set = set()  
   
#        We use SET to:
#     - Check if name exists FAST (O(1) lookup)
#     - Prevent duplicates case-insensitively
#     - "Juan Cruz" and "juan cruz" both become "juan cruz" in set

# IN THIS PROGRAM:
# - student_names (LIST): stores original names for display/sort/search
# - student_set (SET): stores lowercase names for fast duplicate check
# - Both updated together: add to both, remove from both
# - This gives us: fast duplicate check + ordered display + partial search