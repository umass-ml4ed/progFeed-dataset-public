# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}_.txt', 'w') as f:
        for i in range(1, n + 1):
            spaces = ' ' * (n-1)
            stars = '*' * (2 * n-1)
        print(spaces + stars, file=f)
            