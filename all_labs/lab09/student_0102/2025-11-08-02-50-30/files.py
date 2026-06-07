# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(a):
    with open(f"star_{a}.txt", "w") as star:
        star.write(" " * (a-1) + "*")
        for x in range (2,a + 1):
            star.write (" " * (a-x) + "**" * (x-1) + "*" +"/n")
def calc_avg_from_file():
    with open (f"grade.txt") as grade:
        a = grade.read()
        b = a.split('\n')
        c = 0
        for x in b:
            c = c + float(x)
        d = c/len(b)
        return d