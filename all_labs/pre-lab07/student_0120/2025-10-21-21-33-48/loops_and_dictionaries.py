# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        line = ' '.join(str(j) for j in range(i, 0, -1))
        print(line)

print(pyramid(4))
print(pyramid(5))
    