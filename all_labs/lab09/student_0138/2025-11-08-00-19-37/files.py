# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file_star = open(f'stars_{n}.txt', 'w')
    with file_star as f:
        for i in range(1, n+1):
            space = n - i
            stars = 2 * i - 1
            row = (' '*space) + ('*' * stars)
            print(row, file=f)





def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text=f.read()
    split = text.split('\n')
    numbers = [float(p) for p in split if p != '']
    return sum(numbers)/len(numbers)


