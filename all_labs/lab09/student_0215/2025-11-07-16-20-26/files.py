# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(1, n+1):
            num_spaces = n - 1
            num_stars = 2 * i - 1
            line = ' ' * num_spaces + '*' * num_stars
            print(line, file=f)
