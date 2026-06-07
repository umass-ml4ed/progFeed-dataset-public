# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = (' ' * spaces + '*' * stars)
            f.write(line + '\n')

def calc_avg_from_file():
    f = open('grades.txt', 'r')

    text = f.read()
    f.close()
    lst_of_grades = text.split('\n')

    total = 0
    for grade in lst_of_grades:
        total = total + float(grade)

    average = total / len(lst_of_grades)
    return average

