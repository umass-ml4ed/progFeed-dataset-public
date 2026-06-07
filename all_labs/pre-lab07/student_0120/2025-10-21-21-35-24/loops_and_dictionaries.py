# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

def pyramid(n):
    lines = []
    for i in range(n, 0, -1):
        line = ' '.join(str(j) for j in range(i, 0, -1))
        lines.append(line)
    return '\n'.join(lines)

print(pyramid(4))
print(pyramid(5))
    