# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt", "w") as s:
        for x in range(n):
            count_from_zero = x+1
            s.write(((((n - count_from_zero)*" ") + ((2*count_from_zero-1)*"*"))+"\n"))
