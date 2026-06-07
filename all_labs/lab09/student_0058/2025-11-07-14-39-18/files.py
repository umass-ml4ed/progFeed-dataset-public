# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    i = 0
    x = 1

    while x <= n:
        print("*" * x)
        i += 1
