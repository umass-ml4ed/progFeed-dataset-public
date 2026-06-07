# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n + 1):
            line = ' ' * (n-i) + '*' * (2*i-1)
            f.write(line + "\n")
def calc_avg_from_file():
    total = 0
    avg = 0
    with open("grades.txt",'r') as f:
        text = f.read()
        a = text.split('\n')
        for i in range(len(a)):
            b = float(a[i])
            total += b
        avg = total/len(a)
        return avg

