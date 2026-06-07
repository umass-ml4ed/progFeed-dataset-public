# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    for i in range(n):
        f.write((" ")*(n-(i+1)) + "*"*(1+(i)*2))
        if i < n:
            f.write("\n")

def calc_avg_from_file():
    f =  open("grades.txt", "r")
    text = f.read()
    x = text.split("\n")
    undivided = 0
    counter = 0
    for item in x:
        undivided += float(item)
        counter += 1
    return(undivided/counter)
    
    
