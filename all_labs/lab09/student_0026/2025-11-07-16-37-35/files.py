# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open (f'start_{n}.txt', 'w') as file:
        for n in range(1, n+1):
            file.write("*" * n)
            file.write('\n')
    with open (f'start_{n}.txt', 'r') as file:
        print(file.read())

print_stars_to_file(5)