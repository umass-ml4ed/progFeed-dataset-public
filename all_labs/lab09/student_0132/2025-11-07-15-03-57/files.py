# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(n):
    new = f"stars_{n}.txt"
    with open(new, "w") as file:
        for i in range(n):
            numstars = (2*i)+1
            numspace =(n-1)-i
            line=(" "*numspace)+("*"*numstars)
            file.write(line+"\n")
def calc_avg_from_file():
    with open("grades.txt") as f:
        text=f.read()
    gradelist=text.split('\n')
    grades=[]
    for grade in gradelist:
        grades.append(float(grade))
    avg = sum(grades)/len(grades)
    return avg