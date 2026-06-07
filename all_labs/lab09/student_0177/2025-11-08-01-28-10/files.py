# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars, file=f)
def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        grades_list = text.split('\n')
        grades = [float(g) for g in grades_list]
        avg = sum(grades) / len(grades)
        return avg
