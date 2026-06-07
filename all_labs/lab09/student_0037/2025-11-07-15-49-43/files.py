# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file_name = f'stars_{n}.txt'
    with open(file_name, 'w') as f:
        space_char = ' '
        star_char = '*'
        for i in range (1, n+1):
            print(((n-i)*space_char)+((2*i)-1)*star_char, file=f)



def calc_avg_from_file():
    with open('grades.text', 'r') as f:
        text = f.read()
        text.split('\n')
        grades = []
        for grade in text:
            grade = float(grade)
            grades.append(grade)
        avg = sum(grades)/len(grades)
    return avg


