# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = open("./stars_" + str(n) + ".txt", "w")
    num = n
    row = 1
    while row <= n:
        file.write(" " * (n - row))
        file.write("*" * ((2 * row) - 1) + "\n")
        row += 1
