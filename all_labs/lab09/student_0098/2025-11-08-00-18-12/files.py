# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
    grades_str = text.split('\n')
    grades = [float(grade) for grade in grades_str]
    return sum(grades) / len(grades)