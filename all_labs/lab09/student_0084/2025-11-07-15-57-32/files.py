# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#1 Implement function print_stars_to_file
def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            spaces = n - 1 - i
            stars = 2 * i + 1
            line = (' ' * spaces) + ('*' * stars)
            f.write(line)
            if i < n - 1:
                f.write('\n')

#2 Implement function calc_avg_from_file
def calc_avg_from_file():
    with open("grades.txt", 'r') as f:
        text = f.read()
    grade_strings = text.split('\n')
    total = 0.0
    calc_avg = 0.0
    for g in grade_strings:
        total += float(g)
        calc_avg = total / len(grade_strings)
    return calc_avg

