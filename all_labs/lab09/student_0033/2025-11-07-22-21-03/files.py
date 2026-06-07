# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", 'w')
    for i in range(n):
        space = n - i - 1
        stars = 2 * i + 1
        line = ' ' * space + '*' * stars
        print(line, file=f)
    f.close()

def calc_avg_from_file():
    f = open('grades.txt', 'r')
    text = f.read()
    f.close()

    grades = text.split('\n')
    sum = 0
    for i in grades:
        sum += float(i)
    avg = sum / len(grades)
    return avg




