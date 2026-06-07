# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filen= f"stars_{n}.txt"
    with open(filen, 'w') as f:
     for i in range(n):
        space = " " * (n-i-1)
        star = "*" * (2*i+1)
        if i < n-1:
           f.write(space+star+ "\n")
        else:
           f.write(space+star)

def calc_avg_from_file():
   with open("grades.txt", "r") as f:
        txt = f.read().strip()
        grade = txt.split("\n")
        ttl = 0
        for gr in grade:
            ttl += float(gr)
        return ttl / len(grade)
    
        




