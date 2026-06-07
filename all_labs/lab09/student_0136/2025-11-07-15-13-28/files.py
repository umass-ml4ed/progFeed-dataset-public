# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = "stars_" + str(n) + ".txt"
    with open(filename, "w") as f:
        for i in range(1, n+1):
            spaces = n-i
            stars = 2*i-1
            line = " " * spaces + "*" * stars
            f.write(line + "\n")


def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        text = file.read()
        lst = text.split("\n")
        avg = 0
        count = 0
        for i in lst:
            avg += float(i)
            count += 1
        return avg/count
    
