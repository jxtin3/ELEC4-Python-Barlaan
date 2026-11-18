# student_utils.py - Custom Module
# Name: Justine Barlaan
# Section: IV-BSIT B
# Activity Code: P2
# Date: November 18, 2026


# Function 1 to compute average
def compute_average(grades):
    if len(grades) == 0:
        return 0
    total = 0
    for g in grades:
        total = total + g
    return total / len(grades)


# Function 2 to get highest grade
def get_highest(grades):
    if len(grades) == 0:
        return 0
    highest = grades[0]
    for g in grades:
        if g > highest:
            highest = g
    return highest


# Function 3 to get lowest grade
def get_lowest(grades):
    if len(grades) == 0:
        return 0
    lowest = grades[0]
    for g in grades:
        if g < lowest:
            lowest = g
    return lowest


# Function 4 to determine if passorfail
def get_pass_fail(grades):
    avg = compute_average(grades)
    if avg >= 75:
        return "PASS"
    else:
        return "FAIL"