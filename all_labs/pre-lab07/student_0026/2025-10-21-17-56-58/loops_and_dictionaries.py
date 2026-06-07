# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def pyramid(n):
    lines=''
    for a in range(n,0,-1):
        line=''
        for b in range(a,0,-1):
            line+=str(b)
            line+=' '
        lines+=line[:-1] +'\n'
    return lines


print(pyramid(5))
