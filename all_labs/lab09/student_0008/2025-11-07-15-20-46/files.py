# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as file:
        for i in range(1, n+1):
            file.write((' ' * (n-i)) + ('*' * (2*i-1)))

def calc_avg_from_file():
    with open('grades.txt', 'r') as file:
        text=file.read()
        lst = text.split('\n')
        sum = 0
        for i in lst:
            sum += float(i)
        return sum/len(lst)
