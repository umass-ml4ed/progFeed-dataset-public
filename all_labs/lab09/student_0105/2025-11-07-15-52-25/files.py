# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as f:
        for i in range(n):
            print(((n - (i + 1)) * " ") + ((2 * i + 1) * "*"), file = f)

def calc_avg_from_file():
    sum = 0
    with open('grades.txt', 'r') as f:
        text = f.read()
        lst = text.split('\n')
        for i in lst:
            sum += float(i)
    return sum / len(lst)
    
