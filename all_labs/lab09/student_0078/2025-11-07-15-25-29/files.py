#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f'stars_{n}.txt'
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            num_stars = 2 * i - 1
            num_spaces = n - i
            line = ' ' * num_spaces + '*' * num_stars
            f.write(line + '\n')

def calc_avg_from_file():
    filename = 'grades.txt'
    total_sum = 0.0
    count = 0
    
    try:
        with open(filename, 'r') as f:
            text = f.read()
            grades_str_list = text.split('\n')
            grades_str_list = [grade for grade in grades_str_list if grade]
            if not grades_str_list:
                return 0.0 
            for grade_str in grades_str_list:
                try:
                    grade = float(grade_str)
                    total_sum += grade
                    count += 1
                except ValueError:
                    pass
            if count == 0:
                return 0.0
            return total_sum / count
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0.0

