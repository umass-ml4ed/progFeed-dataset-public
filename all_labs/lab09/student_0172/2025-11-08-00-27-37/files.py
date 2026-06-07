# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = ' ' * spaces + '*' * stars
            print(line, file=f)

print_stars_to_file(3)

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        grades = text.split('\n')
        total = 0
        for grade in grades:
            total += float(grade)
        avg = total / len(grades)
        return avg