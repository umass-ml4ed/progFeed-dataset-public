# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    lst = []
    i = 1
    while i <= n:
        s = ' '*(n-i) + '*'*(2*i-1)
        lst.append(s)
        i += 1
    with open(f'stars_{n}.txt', 'w') as file:
        for i in range(0, n):
            file.write(lst[i] + '\n')

def calc_avg_from_file():
    with open('grades.txt', 'r') as file:
        s = file.read()
        grade = s.split('\n')
        return sum(grade)/len(grade)
