# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n+1):
            num_spaces = n - i
            num_stars = 2 * i - 1
            line = ' ' * num_spaces + '*' * num_stars
            print(line, file=f)

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()

    grades_list = text.split('\n')
    total = 0

    for grade_str in grades_list:
        total += float(grade_str)

    average = total / len(grades_list)
    return average