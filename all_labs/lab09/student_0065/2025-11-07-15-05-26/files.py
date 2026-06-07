# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open (filename, "w") as file:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = ' ' * spaces + "*" * stars
            file.write(line + '\n')


def calc_avg_from_file():
    with open('grades.txt', 'r') as file:
        text = file.read()
    grade_strings = text.split('\n')
    grades = [float(g) for  g in grade_strings]
    avg = sum(grades) / len(grades)
    return avg