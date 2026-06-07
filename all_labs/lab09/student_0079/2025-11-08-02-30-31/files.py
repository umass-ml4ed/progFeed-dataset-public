# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{str(n)}.txt", "w") as file:
        count = 1
        while count <= n:
            file.write(" " * (n-count) + "*"*((count-1)*2 + 1) + "\n")
            count += 1

print_stars_to_file(3)
print(open("stars_3.txt", "r").read())

def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        for line in file:
            new_line = line.strip()
        list = []
        list = new_line.split("\n")
    total = 0
    for n in list:
        total += n
    return total / len(list)

print(calc_avg_from_file())