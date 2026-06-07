# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    f = open(f"stars_{n}.txt",'w')
    x=0
    for i in range(1,2*n,2):
        f.write((n-x)*" "+i*"*"+(n-x)*" ")
        x+=1

print_stars_to_file(6) 
