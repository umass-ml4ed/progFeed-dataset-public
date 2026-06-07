# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{str(n)}.txt", "w") as file:
        count = 1
        while count <= n:
            file.write(" " * (n-count) + "*"*((count-1)*2 + 1) + "\n")
            count += 1

print_stars_to_file(5)
print(open("stars_5.txt", "r").read())

def create_grade():
    with open(f"grades.txt", "w") as file:
        file.write("82.5\n")
        file.write("93\n")
        file.write("77.75\n")
        file.write("65\n")

create_grade()

def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        read_file = file.read()
#        for line in read_file:
#            new_line = line.strip()
#        list = []
#        list = new_line.split("\n")
    list = [float(x) for x in read_file.split("\n") if x.strip() != ""]
    total = 0
    for n in list:
        total += n
    return total / len(list)

print(calc_avg_from_file())