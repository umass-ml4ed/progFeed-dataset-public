
# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f'./stars_{n}.txt', 'w') as file:
        for i in range(1, (n+1)):
            space = n -i
            stars = 2 * i - 1
            line = ' ' * space + '*' *stars
            file.write(line + '\n')

def calc_avg_from_file():
    with open(f'grades.txt', 'r') as file:
        total = 0
        count = 0
        for line in file:
            grade = float(line)
            total += grade
            count += 1
        avg = total / count
        return avg