# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    file = open(f"stars_{n}.txt", "w")
    for i in range(n):
        spaces = n - i
        star = (2*i)+1
        print((" " * spaces + "*" * star ), file = file)
        #print(("*" * star + " " * spaces), file = file)

print_stars_to_file(3)
print_stars_to_file(6)




def calc_avg_from_file():
    file = open("grades.txt", "r")
    x = file.read()
    grade = []
    count = 0
    y=0.0
    x.split('\n')
    for i in x:
        #x.split('\n')
        if i.strip() != "":
            y = float(i)
            grade.append(float(i))
            count = count + y
    avg = count/len(grade)
    return avg

print(calc_avg_from_file())

    
