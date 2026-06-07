# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    i = 0
    x = 0
    a = 1 + (2*x)
    while i <= n:
        print("*" * a)
        x += 1
        i += 1
    f.close()
