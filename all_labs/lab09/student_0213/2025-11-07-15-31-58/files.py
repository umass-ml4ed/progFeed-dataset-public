# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    i = 1
    with open(f'stars_{n}.txt', 'w') as f:
        while i in range(1,n+1):
            f.write(' '*(n - i) + '*'*(2*i - 1) + ' '*(n - i) + '\n' + '\n')
            i += 1

print_stars_to_file(4)

def calc_avg_from_file():
    total = 0
    with open('grades.txt', 'r') as f:
        text = f.read()
        text_list = text.split('\n')
        for grade in text_list:
            num_grade = float(grade)
            total += num_grade
    average = total/len(text_list)
    return average