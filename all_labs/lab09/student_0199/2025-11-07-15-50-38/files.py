# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as f:
        for row in range(1, n+1):
            spaces = " " * (n-row) 
            symbols = "*" * (2*row - 1)
            row = (f"{spaces}{symbols}")
            f.write(row+"\n")

print(print_stars_to_file(6))



