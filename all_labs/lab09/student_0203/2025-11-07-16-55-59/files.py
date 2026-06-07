# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(n):
            spaces = n - 1 - i
            stars = 2 * i + 1
            print(" " * spaces + "*" * stars, file=f)

def calc_avg_from_file():
    with open(f"grades.txt", "r") as f:
        text = f.read()
        str_grades = text.split('\n')
        int_grades = []
        for s in range(len(str_grades)):
            int_grades.append(int(s))
        return sum(int_grades) / len(int_grades)
calc_avg_from_file()