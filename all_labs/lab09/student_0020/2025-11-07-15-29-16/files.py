# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt",'w')
    x=1
    for i in range(1,2*n,2):
        f.write((n-x)*" "+i*"*"+(n-x)*" "+"\n")
        x+=1

def calc_avg_from_file():
    f = open("grades.txt",'r')
    text = f.read()
    lst = text.split("\n")
    sum=0
    for number in lst:
        sum+=number
    return sum/len(lst)
