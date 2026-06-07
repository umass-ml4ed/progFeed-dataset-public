# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, "w") as f:
        for i in range(n):
            spaces = n - i - 1
            stars = 2 * i + 1
            line = " " * spaces + "*" * stars
            print(line, file=f)

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        lines = f.read().split("\n")
    total = 0.0
    count = 0
    for grade in lines:
        if grade.strip() != "":
            total += float(grade)
            count += 1
    if count == 0:
        return 0
    return total / count



