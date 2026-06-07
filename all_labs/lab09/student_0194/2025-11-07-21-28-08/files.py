# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'stars_{n}.txt', 'w') as f:
        index = 1
        spaces = n
        stars = 1
        while(index <= n):
            f.write(" " * (spaces - 1))
            if index == n:
                f.write("*" * stars)
            else:
                f.write("*" * stars + "\n")
            index += 1
            stars += 2
            spaces -= 1

