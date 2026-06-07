# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from fileinput import filename


def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            spaces = ' ' * (n - i - 1)
            stars = '*' * (2 * i + 1)
            f.write(spaces + stars + '\n')


def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
    grades_list = text.split('\n')
    grades = [float(num) for num in grades_list]
    avg = sum(grades) / len(grades)
    return avg