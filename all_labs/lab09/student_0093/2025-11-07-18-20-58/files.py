# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    file = 'stars_' + str(n) + '.txt'
    with open(file, 'w') as f:
        i = 1
        while i <= n:
            spaces = n - i
            stars = 2 * i - 1
            line = ' ' * spaces + '*' * stars + '\n'
            f.write(line)
            i += 1

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        strs_lst = text.split('\n')
        grades = []
        for grade in strs_lst:
            grade = float(grade)
            grades.append(grade)
            total = sum(grades)
        avg_grade = total / len(grades)
        return avg_grade


