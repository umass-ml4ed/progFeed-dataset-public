# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(n:int):
    with open(f"stars_{n}.txt", "x") as f:
        for i in range(n,0,-1):
            a=i* " " + "*"*(1+2*(n-i))
            f.write(a+"\n")
    return

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()
        lst = text.split('\n')
        for i in range(len(lst)):
            lst[i]=float(lst[i])
    return sum(lst)/len(lst)
print(calc_avg_from_file())