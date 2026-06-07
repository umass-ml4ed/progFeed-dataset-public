# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


ddef pyramid(n):
    for i in range(n, 0, -1):
        line = ""
        for j in range(i, 0, -1):
            line += str(j) + " "
        print(line.strip())
