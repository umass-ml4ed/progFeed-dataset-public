# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(n):
    for i in range(1, len(n)-1):
        if not ((n[i] > n[i-1] and n[i] > n[i+1]) or (n[i] < n[i-1] and n[i] < n[i+1])):
            return False
    return True