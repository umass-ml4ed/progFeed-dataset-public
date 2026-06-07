# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as file:
        for num in range(1, n):
            file.write(((n - num) * " ") + ((2 * num)-1) * "*" + "\n")

def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        total = []
        for line in file:
            total.append(float(line.strip()))
        return (sum(total)/len(total))