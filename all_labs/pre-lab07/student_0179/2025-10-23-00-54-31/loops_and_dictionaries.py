# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    line = ""
    while n >= 1:
        ns = n
        for ns in range(n,0,-1):
            if ns == 1:
                line = line + str(ns) + "\n"
                break
            else: 
                line = line + str(ns) + " " 
                ns -= 1
        n -= 1
    return line
print(pyramid(4)) 


        