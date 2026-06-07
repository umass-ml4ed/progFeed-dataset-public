# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = f"stars_{n}.txt"
    with open(file, 'w') as f:
        for i in range(1, n + 1):  
            spaces = ' ' * (n - i)          
            stars = '*' * (2 * i - 1)  
            line = spaces + stars           
            print(line, file=f)
