# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open('stars_' + str(n) + '.txt', 'w') as stars:
        for num in range(1, n + 1):
            stars.write(' ' * (n- num) + '*' * (2 * num - 1) + '\n')

def calc_avg_from_file():
    total = 0
    grades = open('grades.txt', 'r').read().split('\n')
    for g in grades:
        total += float(g)
    return total / len(grades)