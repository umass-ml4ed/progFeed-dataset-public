# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = "stars_" + str(n) + ".txt"
    f = open(filename, "w")
    for i in range(n):
        num_spaces = n - 1 - i
        num_stars = 2 * i + 1
        line = " " * num_spaces + "*" * num_stars
        f.write(line + "\n")
    f.close()

def calc_avg_from_file():
    f = open("grades.txt", "r")
    text = f.read()
    f.close()
    grade_strings = text.split("\n")
    grades = []
    for g in grade_strings:
        if g != "":
            grades.append(float(g))
    total = sum(grades)
    count = len(grades)
    average = total / count
    return average