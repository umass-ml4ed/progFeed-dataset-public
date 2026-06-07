# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# create function for making and writing into a file
def print_stars_to_file(n:int):
    stars = list(range(1,2*n, 2))
    with open(f"stars_{n}.txt", "w") as file:
        for line in range(1, n+1):
            file.write(f"{(n-line) * ' '}{stars[line-1]*'*'}\n")
            


