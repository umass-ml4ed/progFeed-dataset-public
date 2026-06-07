# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n: int):
    file_name = f"stars_{n}.txt"
    with open(file_name, 'w') as f:
        for i in range(1, n+1):
            space = ' '*(n-i)
            star = '*'*(2*i-1)
            print(space+star,file=f)

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        grades = text.split('\n')
        float_grades = [float(grade) for grade in grades]
        total = sum(float_grades)
        avg = total/len(float_grades)
        return avg