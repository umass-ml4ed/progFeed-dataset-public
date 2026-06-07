# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(a):
    if len(a)<3:
        return True
    for i in range(1, len(a)-1):
        if not ((a[i-1] < a[i] and a[i]>a[i+1]) or (a[i-1] > a[i] and a[i] < a[i+1])):
            return False
    return True

