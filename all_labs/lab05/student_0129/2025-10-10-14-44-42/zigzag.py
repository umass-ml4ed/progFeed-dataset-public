# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(listy):
    if len(listy) < 3:
        return True

    for i in range(1, len(listy) - 1):
        a, b, c = listy[i - 1], listy[i], listy[i + 1]
        if not ((b > a and b > c) or (b < a and b < c)):
            return False
    return True