# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(l: list):
    if len(l) < 3:
        return True
    for i in range(0, len(l)-2):
        if not(((l[i+1] > l[i] and l[i + 1] > l[i + 2])) or (l[i+1] < l[i] and l[i + 1] < l[i + 2])):
            return False
    return True
    
