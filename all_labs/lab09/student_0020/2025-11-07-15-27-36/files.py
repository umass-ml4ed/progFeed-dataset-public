# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt",'w')
    x=1
    for i in range(1,2*n,2):
        print(n-x)
        f.write((n-x)*" "+i*"*"+(n-x)*" "+"\n")
        x+=1

def calc_avg_from_file():
    f = open("grades.txt",'r')
