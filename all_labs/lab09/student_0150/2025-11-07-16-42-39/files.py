# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    stars = 1
    while stars <= n:
        f.write(" " * (n-stars) + "*"*(stars*2-1) + "\n")
        stars += 1
    f.close()
#print_stars_to_file(6)

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read() 
    grade_strings = text.split('\n')
    total = 0
    count = 0
    for g in grade_strings:
        total = total + float(g)
        count += 1
    average = total / count
    return average
print(calc_avg_from_file())