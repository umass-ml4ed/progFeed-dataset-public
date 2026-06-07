# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    stars_n = f'stars_{n}.txt'
    with open(stars_n, 'w') as file:
        for i in range (n):
            leading_spaces = ' ' * (n - 1 - i)
            stars = '*' * (2 * i + 1)
            file.write(leading_spaces + stars + '\n')

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
    grades_str = text.split('\n')
    grades = [float(grade) for grade in grades_str if grade]
    if grades:
        average = sum(grades) / len(grades)
    else:
        return 0
    return average