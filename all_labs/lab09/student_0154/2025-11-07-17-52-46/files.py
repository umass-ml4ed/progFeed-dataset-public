# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    open('./stars_'+str(n)+'.txt', 'x')
    open('./stars_'+str(n)+'.txt', 'w')
    a = 1
    c = 1
    while a <= n:
        print(" " * (n-a) + "*" * c)
        a += 1
        c += 2

#print(print_stars_to_file(3))

def calc_avg_from_file():
    f = open('./grades.txt', 'r')
    grades = f.read()
    grade_list = grades.split('\n')
    # ['82.5', '93', '77.5', '65']
    float_list = [float(grade) for grade in grade_list]
    total = 0
    for grade_float in float_list:
        total += grade_float
    return (total / len(float_list))

print(calc_avg_from_file())

#DELETE B4 SUBMITING vvv
float_list = [82.5, 93, 77.5, 65]
def calc_avg(lst):
    total = 0
    for grade in lst:
        total += grade
    return (total/len(lst))

#print(calc_avg(float_list))