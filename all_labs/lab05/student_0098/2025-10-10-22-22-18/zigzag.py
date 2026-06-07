# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_zigzag(lst):
    if len(lst) < 3:
        return True

    for i in range(len(lst) - 2):
        if not (lst[i] < lst[i+1] > lst[i+2] or lst[i] > lst[i+1] < lst[i+2]):
            return False

    return True


