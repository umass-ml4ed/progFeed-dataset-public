# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            # (n-1-i) spaces followed by (2*i+1) stars
            spaces = ' ' * (n - 1 - i)
            stars = '*' * (2 * i + 1)
            f.write(spaces + stars + '\n')


def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read().strip()  # remove trailing newline if any
        grades_str = text.split('\n')
        grades = [float(g) for g in grades_str]
        avg = sum(grades) / len(grades)
        return avg
