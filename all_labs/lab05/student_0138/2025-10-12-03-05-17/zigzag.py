# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(list):
    for l in list:
        z = len(list)
        if z < 3:
            return True
        for i in range(1, z-1):
            right = list[i + 1]
            middle = list [i]
            left = list[i - 1]
            if not (middle < left and middle < right) or (middle > left and middle > right):
                return False
        