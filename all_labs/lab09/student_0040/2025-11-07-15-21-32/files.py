# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, "w") as f:
        for i in range(n):
            spaces = n - 1 - i
            stars = 2 * i + 1
            line = " " * spaces + "*" * stars
            f.write(line + "\n")


def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()
        grades_list = text.split("\n")
        total = 0
        count = 0

        for grade in grades_list:
            total += float(grade)
            count += 1

        avg = total / count
        return avg
