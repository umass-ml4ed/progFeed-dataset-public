# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    text = ''
    for i in range(1, int(n + 1)):
        text += ' ' * (int(n) - i + 1)
        text += '*' * (2 * i - 1)
        text += '\n'
    with open(f'stars_{n}.txt', 'w') as stars:
        stars.write(text)
    return

def calc_avg_from_file():
    with open('grades.txt', 'r') as grades:
        raw = grades.read()
        cooked = raw.split('\n')
        cooked = [int(num) for num in cooked]
    return sum(cooked) / len(cooked)

print(calc_avg_from_file())