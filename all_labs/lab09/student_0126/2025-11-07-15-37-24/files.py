# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        g = ''
        for i in range(n):
            g += ' ' * (n - i - 1) + ('*' * (1 + (2 * i)))
            if i != n - 1:
                g += '\n'
        f.write(g)

# print_stars_to_file(7)

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text  = f.read()
        avg = 0
        for i in text.split('\n'):
            avg += float(i)
        avg /= len(text.split('\n'))
        return avg
    
# print(calc_avg_from_file())