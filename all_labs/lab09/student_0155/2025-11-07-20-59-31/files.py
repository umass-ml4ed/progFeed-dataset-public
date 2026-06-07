# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as file:
        count = 1
        while count <= n:
            file.write(' ' * (n-count) + '*' * ((count*2)-1) + '\n')
            count += 1
        pass

#print_stars_to_file(3)

def calc_avg_from_file():
    with open('grades.txt', 'r') as file:
        count = 0
        total = 0
        for line in file:
            grade = line.strip('\n')
            total += float(grade)
            count += 1
        pass
    return total / count

#print(calc_avg_from_file())

