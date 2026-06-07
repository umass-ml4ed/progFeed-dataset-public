# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def pyramid(n):
    for a in range(n,0,-1):
        line=''
        for b in range(a,0,-1):
            line+=str(b)
            line+=' '
        print(line[:-1])


pyramid(4)
