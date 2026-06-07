# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n): 
    file_name = f"stars{n}.txt" #f string for different n values 
    with open(file_name, 'w') as f: 
        for i in range(1, n+1): 
            spaces = " " * (n-1) 
            stars = "*" * (2*i-1)
            f.write(spaces + stars + "\n")

print_stars_to_file(3)