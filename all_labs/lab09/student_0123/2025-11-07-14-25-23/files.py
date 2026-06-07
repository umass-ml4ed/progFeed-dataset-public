# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open("stars_" + str(n) + ".txt", "w") as file:
        for i in range(n):
            file.write(" " * (n - i - 1) + "*" * (2 * i + 1) + "\n")


def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        text = file.read()
        text = text.split("\n")
        floated = []
        for i in text:
            floated.append(float(i))
        return sum(floated) / len(floated)