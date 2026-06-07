# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as file:
        for i in range (1, n+1):
            line = (n-i)*' ' + (2*i-1)*'*'
            print(line, file=file)

def calc_avg_from_file():
    with open('grades.txt', 'r') as file:
        text = file.read()
        grades = text.split('\n')
        total = 0
        num = 0
        for grade in grades:
            total += float(grade)
            num += 1
        return total/num