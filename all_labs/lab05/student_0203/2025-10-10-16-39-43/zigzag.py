# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) < 3:
        return True
    for i in range(1, len(list) - 1):
        if not (list[i] > list[i + 1] and list[i] > list[i - 1]) or (list[i] < list[i + 1] and list[i] < list[i - 1]):
            return False
    return True

