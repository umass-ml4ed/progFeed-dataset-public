# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
        line = " ".join(str(j) for j in range(i, 0, -1))
        result += line + "\n"
    return result

print(pyramid(4))