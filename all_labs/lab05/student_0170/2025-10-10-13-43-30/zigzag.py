# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) < 3:
        return True
    for i in range(1,len(list)-1):
        if (list[i] > list[i-1]) and (list[i] > list[i+1]):
            continue
        elif (list[i] < list[i-1]) and (list[i] < list[i+1]):
            continue
        else:
            return False
    return True