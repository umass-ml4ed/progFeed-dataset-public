#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    
    with open(filename, 'w') as file:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = ' ' * spaces + '*' * stars
            file.write(line)
            if i != n:  
                file.write('\n')

def calc_avg_from_file():
    with open("grades.txt", 'r') as f:
        text = f.read()
    
    grades_list = text.split('\n')
    
    total = 0.0
    for grade in grades_list:
        total += float(grade)
    
    avg = total / len(grades_list)
    return avg
