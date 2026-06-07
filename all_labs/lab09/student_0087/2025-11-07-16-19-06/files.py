# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file (n):
    with open ('stars_n.txt', 'w') as f:
        x = 2*n-1
        for i in range (n):
            spaces = '' * (n-i-1)
            stars = '*' * (2 * (n-1) - 1)
            lines = spaces + stars
            print (lines)
            f.write (lines + '\n')
print (print_stars_to_file(4))