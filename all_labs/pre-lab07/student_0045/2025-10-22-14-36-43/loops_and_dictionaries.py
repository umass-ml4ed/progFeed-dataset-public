# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        for z in range(i, 0, -1):
            print(z, end=" ")
        print()

pyramid(4)