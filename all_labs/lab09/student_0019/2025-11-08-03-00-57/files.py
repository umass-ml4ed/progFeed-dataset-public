# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as f:
        for i in range(1, n + 1):
            gaps = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
        
            print(gaps + stars, file=f)

def calc_avg_from_file(): 
    with open('grades.txt', 'r') as f:
        text = f.read()
        grade_strings = text.split('\n')
        total_sum = 0.0
        grade_count = 0
        for grade_str in grade_strings:
            if grade_str != str():
                grade = float(grade_str)
                total_sum += grade
                grade_count += 1

        if grade_count > 0:
            return total_sum / grade_count 
        else: 
            return 0.0