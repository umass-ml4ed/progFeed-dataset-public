# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(x):
    if len(x) < 3:
        return True

    for i in range(1, len(x) - 1):
        left = x[i - 1]
        mid = x[i]
        right = x[i + 1]

        if (mid > left and mid > right) or (mid < left and mid < right):
            continue
        else:
            return False

    return True
