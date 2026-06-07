# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from typing import NoReturn

def print_stars_to_file(n:int):
    filename = f"stars_{n}.txt"
    with open(filename,"w",encoding="utf-8") as f:
        for i in range(1,n+1):
            spaces=" "*(n-i)
            stars="*"*(2*i-1)
            f.write(spaces+stars+"\n")

print_stars_to_file(3)
print_stars_to_file(6)

def calc_avg_from_file():
    with open("/Users/kexinjiang/Desktop/CICS 110/lab 09/grades.txt","r",encoding="utf-8") as f:
        text=f.read()
    parts=[p for p in text.split("\n") if p!=""]
    nums=[float(p) for p in parts]
    return sum(nums)/len(nums)

print(calc_avg_from_file())
