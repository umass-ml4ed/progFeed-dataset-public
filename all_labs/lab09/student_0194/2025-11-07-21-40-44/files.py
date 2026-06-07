# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as f:
        index = 1
        spaces = n
        stars = 1
        while(index <= n):
            f.write(" " * (spaces - 1))
            if index == n:
                f.write("*" * stars)
            else:
                f.write("*" * stars + "\n")
            index += 1
            stars += 2
            spaces -= 1

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        lst = text.split('\n')
        sum = 0
        for i in lst:
            i = float(i)
            sum += i
        return sum / len(lst)