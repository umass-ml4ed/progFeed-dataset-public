# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n): 
    filename = f'stars_{n}.txt'
    with open(filename,'w') as f:
            for i in range(1, n + 1):
                spaces = ' ' * (n - i)
                stars = '*' * (2 * i - 1)
                print(f'{spaces}{stars}', file=f)

def calc_avg_from_file():
    f = open('grades.txt', 'r')
    text = f.read()
    f.close()
    
    grades_list = text.split('\n')
    total = 0
    count = 0
    for grade in grades_list:
        if grade.strip():
            total += float(grade)
            count += 1
    average = total / count if count > 0 else 0
    return average