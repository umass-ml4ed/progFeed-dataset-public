# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f'stars_{n}.txt', 'w')
    for i in range(1,n+1):
        print(f' '*(n-i) + '*'*(i*2-1), file=f)

print_stars_to_file(2)

def calc_avg_from_file():
    f = open('grades.txt', 'r')
    print(f)
    text = f.read()
    print(text)
    lst = text.split('\n')
    print(lst)
calc_avg_from_file()