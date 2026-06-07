# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(q):
    if len(q) < 3:
        return True
    for i in range(1, len(q) - 1):
        if not ((q[i] > q[i-1] and q[i] > q[i+1]) or (q[i] < q[i-1] and q[i] < q[i+1])):
            return False
    return True
