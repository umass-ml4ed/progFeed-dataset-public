# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) <= 3:
        return True
    for x in range(1, len(list) - 1):
        if (list [x] >= list[x + 1] and list[x] >= list[x - 1]) or (list[x] <= list[x - 1] and list[x] <= list[x + 1]):
            continue
        else:
            return False
    return True