# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f'./stars_{n}.txt','w') as file:
        for line in range(1,n):
            file.write(" " * (n - line) + '*' * (line + (line - 1)) + "\n")
        file.write('*' * (2 * n - 1))

print_stars_to_file(6)