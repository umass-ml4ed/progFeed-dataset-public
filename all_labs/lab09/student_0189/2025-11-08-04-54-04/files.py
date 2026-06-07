# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            spaces = ' ' * (n - 1 - i)
            stars = '*' * (2 * i + 1)
            f.write(spaces + stars + '\n')

def calc_avg_from_file():
    with open("grades.txt", 'r') as f:
        text = f.read()
        grades = text.split('\n')
        total = 0
        count = 0
        for grade in grades:
            if grade.strip() != '':
                total += float(grade)
                count += 1
        return total / count
