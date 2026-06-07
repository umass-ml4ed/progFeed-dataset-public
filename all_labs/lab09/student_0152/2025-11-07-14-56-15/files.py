# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    count = 1
    with open(f'./stars_{n}.txt', 'w') as file:
        for num in range(1, n + 1):
            file.write(f'{" " * (n - num)}{"*" * count}\n')
            count += 2

def calc_avg_from_file():
    with open('./grades.txt', 'r') as file:
        text = file.read()
        grades = text.split('\n')
        total = 0
        for grade in grades: 
            total += float(grade)
    return total / len(grades)
    
print(calc_avg_from_file())