# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n: int):
    with open(f'stars_{n}.txt', 'w') as file:
        for i in range(1, n + 1):
            spaces = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            file.write(spaces + stars + '\n')
    return

print_stars_to_file(4)





