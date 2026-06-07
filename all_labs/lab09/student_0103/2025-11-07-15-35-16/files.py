# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as file:
        i = 1
        while i < n:
            spaces = " " * (n - i)
            stars = "*" * (i * 2 - 1)
            file.write(f"{spaces}{stars}\n")
            i = i + 1
        if i == n:
            stars = "*" * (n * 2 - 1)
            file.write(f"{stars}")


def calc_avg_from_file():
    f = open("grades.txt", "r")
    text = f.read()
    text.split("\n")
    sum = 0
    count = 0
    for i in text.split("\n"):
        sum = sum + float(i)
        count = count + 1
    f.close
    return sum / count