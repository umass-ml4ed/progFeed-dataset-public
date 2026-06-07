# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file (n):
    file = f"stars_{n}.txt"
    with open (file, 'w') as f:
        x = 2*n-1
        for i in range (n):
            spaces = ' ' * (n-i-1)
            stars = '*' * (2 * n + 1)
            lines = spaces + stars
            f.write (lines + '\n')
            print (lines)
print (print_stars_to_file(4))