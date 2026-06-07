# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    
    with open(filename, "w") as f:
        for i in range(1, n+1):
            space = n - i
            star = 2*i - 1
            line = " " * space + "*" * star
            f.write(line + "\n")
#print_stars_to_file(3)
#print_stars_to_file(8)

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()                

    part = text.split("\n")          
    total = 0
    for i in part:
        total += float(i)          

    avg = total / len(part)       
    return avg
#print(calc_avg_from_file())