# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f'stars_{n}.txt'
    file_obj = open(filename, 'w')
    
    for line_num in range(n):
        spaces = n - line_num - 1
        stars = 2 * line_num + 1
        
        line_content = ' ' * spaces + '*' * stars
        file_obj.write(line_content + '\n')
    
    file_obj.close()


def calc_avg_from_file():
    file_obj = open('grades.txt', 'r')
    text = file_obj.read()
    file_obj.close()
    
    grades_list = text.split('\n')
    total = 0
    count = 0
    
    for grade_str in grades_list:
        if grade_str:  # Skip empty strings
            total += float(grade_str)
            count += 1
    
    average = total / count
    return average