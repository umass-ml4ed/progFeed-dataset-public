# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
    
import os
print(os.getcwd())

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n+1):
            line = ' ' * (n - i) + '*' * (2*i - 1)
            print(line, file=f)


import os

def calc_avg_from_file():
    # Build the path to grades.txt relative to THIS .py file
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'grades.txt')

    with open(path, 'r') as f:
        text = f.read()

    # Split safely and ignore empty/whitespace-only lines
    items = [s.strip() for s in text.splitlines() if s.strip() != '']

    nums = [float(s) for s in items]
    return sum(nums) / len(nums)


