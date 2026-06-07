# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            f.write(spaces + stars)
            if i != n: 
                f.write('\n')


def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read().strip() 

    
    grades = [float(x) for x in text.split('\n') if x != '']

   
    return sum(grades) / len(grades)
