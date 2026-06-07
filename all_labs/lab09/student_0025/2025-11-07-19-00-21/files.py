# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file_1 = f'stars_{n}.txt'
    with open(file_1, 'w') as file:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            file.write(spaces + stars + '\n')

def calc_avg_from_file():
    with open('grades.txt', 'r') as file:
        text = file.read()
        strings = text.split('\n')
        grades = [float(x) for x in strings]

    average = sum(grades) / len(grades)
    return average
