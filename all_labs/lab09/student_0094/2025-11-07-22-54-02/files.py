# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def print_stars_to_file(n):
    filename = f"stars_{n}.txt"

    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = n - i          
            stars = 2 * i - 1       
            f.write(' ' * spaces + '*' * stars + '\n')

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
    grade_strings = text.split('\n')
    total = 0.0
    for s in grade_strings:
       total += float(s)

    return total / len(grade_strings)


print(print_stars_to_file(6))
print(calc_avg_from_file())