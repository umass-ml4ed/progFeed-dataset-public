# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) <= 2:
        return True
    for integer in range(1, len(list)):
        if integer == len(list) - 1:
            break
        elif ((list[integer] > list[integer - 1] and list[integer] > list[integer + 1]) or (list[integer] < list[integer - 1] and list[integer] < list[integer + 1])):
            continue
        else:
            return False
    return True

