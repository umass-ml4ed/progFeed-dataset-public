# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", 'w') as f:
        for i in range(1, n+1):
            spaces = n - i
            stars = 2 * i - 1
            f.write(' ' * spaces + '*' * stars + '\n')


def calc_avg_from_file():
    with open('grades.tex', 'r') as f:
        text = f.read()
        lst = text.split('\n')
        grades = [float(g) for g in lst]
        avg = sum(grades) / len(grades)
        return avg