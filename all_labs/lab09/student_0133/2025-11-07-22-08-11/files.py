# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, "w") as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = " " * spaces + "*" * stars
            f.write(line + "\n")
#print_stars_to_file(3)
#print_stars_to_file(6)



def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()
        grade_strings = text.split("\n")
        grades = [float(g) for g in grade_strings]
        average = sum(grades) / len(grades)
        return average
    
print(calc_avg_from_file())


