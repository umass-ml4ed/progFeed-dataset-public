# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt","w") as f:
        for i in range(n):
            f.write(' '*(n-i-1)+'*'*(2*i+1)+'\n')

def calc_avg_from_file():
    with open("grades.txt","r") as f:
        l=[float(i) for i in f.readlines()]
        return sum(l)/len(l)
