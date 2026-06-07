# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = f"stars_{n}.txt"
    f = open(file, 'w')
    for i in range(1, n + 1):
            spaces = n - i 
            stars = 2 * i -1 
            line = " " * spaces + "*" * stars
            f.write(line + "\n")
    f.close()
def calc_avg_from_file(filename): 
    with open(filename, 'r') as f:
        text = f.read()
        grades = text.split("\n")
        total = 0 
        for grade in grades:
            total += float(grade)
        return total / len(grades)


