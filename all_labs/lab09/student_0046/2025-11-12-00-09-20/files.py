# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n: int):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(1, 1+n):
            f.write('*'*i + "\n")

print_stars_to_file(3)           

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text= f.readlines()
        grades= []
        for i in text:
            grades.append(float(i.strip('\n')))
    avg = sum(grades)/ len(grades)
    print(avg)

calc_avg_from_file()
        

