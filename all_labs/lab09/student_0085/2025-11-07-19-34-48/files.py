# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from fileinput import filename


def print_starts_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            spaces = ' ' * (n - i - 1)
            stars = '*' * (2 * i + 1)
            f.write(spaces + stars + '\n')