# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open (f'stars_{n}.txt', 'w') as file:
        file.write((n-1) * "\t" + '*')
        file.write((n-2) * "\t" + '***')
        file.write((n-3) * "\t" + '*****')

def calc_avg_from_file():
    with open ('grades.txt', 'r') as f:
        text = f.read()
        grades = text.split("\n")
        total_grade = 0
        count = 0
        for grade in grades:
            total_grade += float(grade)
            count += 1
        avg_grade = total_grade / count
        return avg_grade

