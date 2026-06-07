# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) < 3:
        return True
    if len(list) == 0:
        return False
    i = 1
    for i in range(len(list) - 1):
        if (list[i] > list[i + 1] and list[i] > list[i - 1]) or (list[i] < list[i + 1] and list[i] < list[i - 1]):
            i += 1
        else:
            return False
    return True

