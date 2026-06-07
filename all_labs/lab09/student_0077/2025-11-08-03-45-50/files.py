# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
import random
def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(1,n+1):
            space= n-i
            star= 2*i-1
            out= " "*space + "*"*star
            f.write(out+ "\n")

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text= f.read()
    grade= text.split("\n")
    grades=[]
    for a in grade:
        removed= a.strip()
        if removed:
            grades.append(float(removed))
    if grades:
        return sum(grades)/len(grades)
    else: 
        return 0