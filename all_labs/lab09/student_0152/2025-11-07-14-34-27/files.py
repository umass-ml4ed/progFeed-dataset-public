# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    count = 1
    with open(f'./stars_{n}.txt', 'w') as file:
        for num in range(1, n + 1):
            file.write(f'{" " * (n - num)}{"*" * count}\n')
            count += 2

print_stars_to_file(6)