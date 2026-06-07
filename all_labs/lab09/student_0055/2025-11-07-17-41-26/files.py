# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = f"stars_{n}.txt"
    with open (file, 'w') as f:
        for i in range(1, n+1):
            f.write(((n-i) * " ") + (((2 * i) - 1) * "*") + "\n")

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

