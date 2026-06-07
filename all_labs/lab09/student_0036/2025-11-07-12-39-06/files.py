# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n:int):
    with open(f"Lab 09/stars_{n}.txt", "w") as f:
        for i in range(1,n+1):
            space=n-i
            stars=(2*i)-1
            print(" "*space+"*"*stars,file=f)

def calc_avg_from_file():
    with open("Lab 09/grades.txt","r") as f:
        text=f.read()
        grades=text.split('\n')
        sum = 0
        for i in grades:
            sum+=float(i)
        return sum/len(grades)

