# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for i in range(n):
            spaces = n - 1 - i
            stars = 2 * i + 1
            line = " " * spaces + "*" * stars
            f.write(line + "\n")
print_stars_to_file(3)
