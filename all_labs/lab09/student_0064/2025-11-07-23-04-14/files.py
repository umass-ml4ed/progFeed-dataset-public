# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED

def print_stars_to_file(n):
    open(stars_n.txt)

    def print_stars_to_file(n):
    starsfile = f"stars_{n}.txt"
    with open(starsfile, 'w') as f:
        for i in range(1, n + 1):
            stars = 2 * i - 1
            spaces = n - i
            line = ' ' * spaces + '*' * stars
            print(line, file=f)

def calc_avg_from_file():
    with open('grades.txt', 'r') as f:
        text = f.read()
    grades = text.split('\n')
    grades = [float(g) for g in grades if g.strip() != '']
    avg = sum(grades) / len(grades)

    return avg
