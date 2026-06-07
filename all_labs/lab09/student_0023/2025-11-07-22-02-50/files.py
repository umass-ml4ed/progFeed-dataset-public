# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1
        f.write(" " * spaces + "*" * stars + "\n")
    f.close()

def calc_avg_from_file():
    f = open("grades.txt", "r")
    text = f.read()
    f.close()
    grades = text.split("\n")
    total = 0
    for g in grades:
        total += float(g)
    return total / len(grades)
