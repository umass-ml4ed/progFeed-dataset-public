# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_starts_to_file(n):
    filename = f"stars_{n}.txt"
    with open (filename, "w") as file:
        for i in range(1, n + 1):
            spaces = n - i
            stars = 2 * i - 1
            line = ' ' * spaces + "*" * stars
            file.write(line + '\n')
