# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    for i in range(n, 0,-1):
        for j in range(i, 0,-1):
            print(j, end =" ")
        print()
pyramid(8)