# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n: int):
    file_name = f"stars_{n}.txt"
    with open(file_name, 'w') as f:
        for i in range(1, n+1):
            space = ' '*(n-1)
            star = '*'*(2*i-1)
            print(space+star,file=f)


print_stars_to_file(3)