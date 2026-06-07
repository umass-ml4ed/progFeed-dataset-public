# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n: int) -> None:
    filename = f"stars_{n}.txt"
    with open(filename, 'w') as f:
        for i in range(n):
            line = '' * (n - 1 - i) + '*' * (2 * i + 1)
            print(line, file=f)