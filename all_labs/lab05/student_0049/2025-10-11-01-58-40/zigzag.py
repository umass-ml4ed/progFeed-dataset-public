# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(x):
    if len(x) < 3:
        return True
    for i in range(1, len(x) - 1):
        if not ((x[i] > x[i - 1] and x[i] > x[i + 1]) or (x[i] < x[i - 1] and x[i] < x[i + 1])):
            return False
    return True
