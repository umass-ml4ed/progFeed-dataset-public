# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as file:
        for i in range(1, n + 1):
            file.write(" " * (n - i) + "*" * (2 * i - 1) + "\n")

def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        text=file.read()
        text_by_line = text.split("\n")
        total = 0
        divisor = 0
        for line in text_by_line:
                total += float(line)
                divisor += 1
        average = total / divisor
    return average