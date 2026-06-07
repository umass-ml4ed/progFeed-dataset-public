# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    newfile = f"stars_{n}.txt"
    with open(newfile, 'w') as x:
        for i in range(1, n+1):
            s = '*' * (2* i-1)
            b = ' ' * (n-i)
            x.write(b + s +'\n')
print_stars_to_file(3)

def calc_avg_from_file():
    with open('grades.txt', 'r') as x:
        t = x.read()
    string = t.split('\n')
    grade = []
    for i in string:
        if i != '':
            grade.append(float(i))
    avg = sum(grade)/len(grade)
    return avg
print(calc_avg_from_file())