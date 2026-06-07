# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as f:
        for i in range(n):
            print(((n - (i + 1)) * " ") + ((2 * i + 1) * "*"), file = f)

print_stars_to_file(3)