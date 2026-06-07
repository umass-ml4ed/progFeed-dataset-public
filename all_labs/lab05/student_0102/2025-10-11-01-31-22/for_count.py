# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def count_strings(n,v):
    b=0
    for x in range (0,len(n)):
        a = n[x]
        if len(a) >= v:
            b = b+1
    return (b)


