# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    result = ""
    for i in range(n):
        line1 = [str(x) for x in range(n-i, 0, -1)]
        result+=' '.join(line1) + "\n"
    return result

print(pyramid(4))

