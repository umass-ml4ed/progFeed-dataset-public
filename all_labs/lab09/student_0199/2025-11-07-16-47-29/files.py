# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for row in range(1, n+1):
            spaces = " " * (n-row) 
            symbols = "*" * (2*row - 1)
            line = (f"{spaces}{symbols}")
            f.write(line+"\n")

#print(print_stars_to_file(7))

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()
        lst = text.split("\n")
    total = 0
    count = 0
    for grade in lst:
        if grade != "":
            total += float(grade)
            count += 1
    return total/count
    
#print(calc_avg_from_file())







