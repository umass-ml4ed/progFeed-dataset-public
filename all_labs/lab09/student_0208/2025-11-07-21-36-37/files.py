# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as stars:
        for i in range(1,n+1):
            b=' '*(n-i)
            s='*'*(2*i-1)
            stars.write(b+s+'\n')

def calc_avg_from_file():
    with open("grades.txt", "r") as file:
        text=file.read()
        grade=text.split('\n')
        grades=[]

        for g in grade:
            if g !='':
                grades.append(float(g))

        avg=sum(grades)/len(grades)
        return avg