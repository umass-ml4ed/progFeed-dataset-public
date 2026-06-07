# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    stars = 1
    while stars <= n:
        f.write(" " * (n-stars) + "*"*(stars*2-1) + "\n")
        stars += 1
    f.close()
print_stars_to_file(6)
