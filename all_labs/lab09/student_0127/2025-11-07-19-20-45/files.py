# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            f.write(spaces + stars + '\n')

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read()
    
    grades_str = text.split('\n')
    
    grades = [float(g) for g in grades_str if g.strip() != '']
    
    if len(grades) == 0:
        return 0  # No ZeroDivisionError
    return sum(grades) / len(grades)
