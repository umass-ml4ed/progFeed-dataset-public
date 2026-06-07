# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n+1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            if i <= n - 1:
                f.write(spaces + stars + '\n')
            else:
                f.write(spaces + stars)
           
print_stars_to_file(5)

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        grades_list = [line for line in text.split('\n') if line.strip() != '']
        grades = [float(g) for g in grades_list]
        avg = sum(grades) / len(grades)
        return avg