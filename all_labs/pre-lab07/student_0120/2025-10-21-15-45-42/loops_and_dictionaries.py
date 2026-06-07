# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

def pyramid(n):
    s = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            s += str(j) + " "
        s += "\n"
    return s

print(pyramid(7))

    