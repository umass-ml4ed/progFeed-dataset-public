# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    counter = 1
    counterstars = 1
    while counter < n:
        print(" " * (n - counter) + ("*" * counterstars))
        counter += 1
        counterstars += 2
    if counter == n:
        print("*" * (2 * n - 1))