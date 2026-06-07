# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = open(f"stars_{n}.txt", 'x')
    x = 0
    while x < (n-1):
        print(((' ' * (n-(x+1))) + (2 * x + 1) * '*'), file = file)
        x += 1
    print(((2 * n-1) * '*'), file = file)

def calc_avg_from_file():
    file = open('grades.txt', 'r')
    text = file.read()
    list = text.split('\n')
    count = 0
    for i in list:
        count += float(i)
    return count / len(list)



    
