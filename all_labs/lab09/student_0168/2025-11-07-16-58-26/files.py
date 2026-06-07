# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(n):
    count=1
    star=1
    file=open(f"stars_{n}.txt", "w")
    while n>=count:
        spaces=(n-count)*" "
        stars=star*"*"
        spandst=f"{spaces}{stars}\n"
        file.write(spandst)
        count+=1
        star+=2

print_stars_to_file(3)

def calc_avg_from_file():
    file=open("grades.txt", "r")
    text=file.read()
    grades = text.split('\n')
    gradess=[]
    for grade in grades:
        gradess.append(float(grade))
    average=sum(gradess)/len(gradess)
    return average
#print(calc_avg_from_file())

