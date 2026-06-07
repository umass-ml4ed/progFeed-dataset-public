 # Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = ' ' * spaces + '*' * stars
            print(line, file=f)

def calc_avg_from_file():
    with open("grades.txt", 'r') as f:
        text = f.read()
        grades_str = text.split('\n')
        grades = [float(g) for g in grades_str if g != '']
        return sum(grades) / len(grades)