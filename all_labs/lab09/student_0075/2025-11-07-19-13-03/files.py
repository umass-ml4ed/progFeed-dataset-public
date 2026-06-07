# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    
    file = (f"stars_{n}.txt")
    with open(file, 'w') as f:
        for i in range(1, n + 1):
            s1 = ' ' * (n - i)
            s2 = '*' * (2 * i - 1)
            f.write(s1 + s2 + '\n')

def calc_avg_from_file():

    total = 0.0
    count = 0
    with open("grades.txt", "r") as f:
        for line in f:
            s = line.strip()
            if s:
                total += float(s)
                count += 1
    return total / count

