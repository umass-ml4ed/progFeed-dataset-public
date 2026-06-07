# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f: 
        for i in range(n):
            spaces = n - 1 - i
            stars = 2* i + 1
            line = (" " * spaces) + ("*" * stars)
            f.write(line)
            if i < n -1: 
                f.write('\n')

def calc_avg_from_file():
    with open("grades.txt", 'r') as f:
        text = f.read().strip()
    grades = text.split('\n')
    total = 0
    for grade in grades:
        total += float(grade)
    return total / len(grades)

print(calc_avg_from_file())