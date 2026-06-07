# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open (f'stars_{n}.txt', 'w') as file:
        for x in range(1, n+1):
            file.write(' ' *(n+1))
            file.write('*' *( 2*x-1))
            file.write('\n')

print_stars_to_file(5)