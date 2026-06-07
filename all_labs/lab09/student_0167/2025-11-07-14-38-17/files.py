def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    
    with open(filename, 'w') as file:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = ' ' * spaces + '*' * stars
            file.write(line + '\n')

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
    
    grades_list = text.split('\n')
    
    total = 0
    for grade_str in grades_list:
        total += float(grade_str)
    
    average = total / len(grades_list)
    
    return average