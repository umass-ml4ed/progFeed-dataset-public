# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = f"stars_{n}.txt"
    with open(file, 'w') as file:
        for x in range(1, n + 1):
            nspaces = ' ' * (n - x)
            nstars = '*' * ((2 * x) - 1)
            file.write(nspaces + nstars + '\n')

def calc_avg_from_file():
    with open('grades.txt', 'r') as file:
        text = file.read()
        gradeswords = text.split('\n')
        gradesnum = [float(g) for g in gradeswords]
        avg = sum(gradesnum) / len(gradesnum)
        return avg