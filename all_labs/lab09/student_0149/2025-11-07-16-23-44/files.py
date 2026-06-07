# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    filename = (f"stars_{n}.txt")
    openfile = open(filename,"w")
    for num in range(1,n+1):
        openfile.write((((n-(num))*" ") + ("*" * (1 + (2 * (num-1))))) + "\n")
    openfile.close()

print(print_stars_to_file(4))