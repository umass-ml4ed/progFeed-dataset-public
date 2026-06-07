# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from fileinput import filename


def print_stars_to_file(n):
    """
    Create a file /mnt/data/stars_n.txt containing an n-line centered triangle of stars.
    Each line i (0-based) has (n-i-1) leading spaces and (2*i+1) stars.
    """
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            spaces = ' ' * (n - i - 1)
            stars = '*' * (2 * i + 1)
            f.write(spaces + stars + '\n')


def calc_avg_from_file():
    filename = "numbers.txt"
    total = 0
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            try:
                num = float(line.strip())
                total += num
                count += 1
            except ValueError:
                continue
    if count > 0:
        avg = total / count
        print(f"Average: {avg}")
    else:
        print("No valid numbers found.")