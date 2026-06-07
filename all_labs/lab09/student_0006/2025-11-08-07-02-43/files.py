# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open (f"stars_{n}.txt", "w") as f:
        for x in range(1, n+1):
            blank = " "*(n-x)
            star = "*"*(2*x-1)
            print(blank + star, file=f)
            
def calc_avg_from_file():
    with open ("grades.txt", "r") as f:
        text = f.read().strip
        grades = text.split("\n")
        total = 0.0
        for mark in grades:
            total += float(mark)
    return total/len(grades)
        