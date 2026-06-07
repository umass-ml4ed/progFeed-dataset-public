# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'x') as f:
        for i in range(1, n+1):
            f.write((' ' * (n-i)) + ('*' * (2*i-1)) + '\n')
    return 

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read().split('\n')
        grades = []
        for grade in text:
            grades.append(float(grade))
        avg = sum(grades)/len(grades)
    return avg
print(calc_avg_from_file())