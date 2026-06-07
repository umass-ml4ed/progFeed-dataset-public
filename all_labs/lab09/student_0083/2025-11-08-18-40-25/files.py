# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            f.write(spaces + stars + '\n')


def calc_average_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
        text.split('\n')
        for i in text:
            average = []
            float_i = float(i)
            average.append(float_i)
        average = sum(average) / len(average)
    return average

