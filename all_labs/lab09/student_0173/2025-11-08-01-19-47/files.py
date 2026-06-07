# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f'stars_{n}.txt', 'w')
    for i in range(1,n+1):
        print(f' '*(n-i) + '*'*(i*2-1), file=f)

def calc_avg_from_file():
    f = open('grades.txt', 'r')
    text = f.read()
    lst = text.split('\n')
    sum = 0
    for i in lst:
        sum += i
    return sum/len(lst)
