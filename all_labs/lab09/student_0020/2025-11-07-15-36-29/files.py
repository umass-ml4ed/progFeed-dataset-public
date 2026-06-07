# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt",'w')
    for i in range(1,n+1):
        f.write((n-i)*" "+(2*i-1)*"*"+"\n")

def calc_avg_from_file():
    f = open("grades.txt",'r')
    text = f.read()
    lst = text.split("\n")
    sum=0
    for number in lst:
        sum+=float(number)
    return sum/len(lst)
