# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open("Stars_" + str(n) + ".txt", "w") as file:
        for i in range(n):
            file.write(" " * (n - i - 1) + "*" * (2 * i + 1) + "\n")

print_stars_to_file(5)