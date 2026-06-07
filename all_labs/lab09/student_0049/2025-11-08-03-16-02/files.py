# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, "w") as file:
        for i in range(n):
            spaces = ' ' * (n - 1 - i)
            stars = '*' * (2 * i + 1)
            file.write(spaces + stars + '\n')

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()
        grade_strings = text.split('\n')
        grades = [float(g) for g in grade_strings if g.strip() != '']
        average = sum(grades) / len(grades)
        return average