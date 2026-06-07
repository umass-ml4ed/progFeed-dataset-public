# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open('./myfile.txt', 'w') as s:
        counter = 1
        counterstars = 1
        while counter < n:
            s.write(" " * (n - counter) + ("*" * counterstars))
            s.write('\n')
            counter += 1
            counterstars += 2
        if counter == n:
            s.write("*" * (2 * n - 1))
