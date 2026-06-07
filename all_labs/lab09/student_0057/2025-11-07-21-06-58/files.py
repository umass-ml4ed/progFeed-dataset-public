# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars, file=f)
print_stars_to_file(6)

def calc_avg_from_file():
    """Reads grades.txt, calculates, and returns the average of all numbers."""
    with open('grades.txt', 'r') as f:
        text = f.read()
        grades_str = text.split('\n')
        grades = [float(g) for g in grades_str]
        avg = sum(grades) / len(grades)
        return avg

