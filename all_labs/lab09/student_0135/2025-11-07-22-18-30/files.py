# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            f.write(spaces + stars)
            if i != n:
                f.write('\n')

#print_stars_to_file(3)

def calc_avg_from_file():
    with open("grades.txt", "r") as f:
        text = f.read().strip()
    grades = text.split('\n')
    grades = [float(g) for g in grades if g]
    avg = sum(grades)/len(grades)
    return avg

#print(calc_avg_from_file())