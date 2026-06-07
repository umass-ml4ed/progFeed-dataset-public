# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_zigzag(lst):
    if len(lst) < 3:
        return True

    for i in range(1, len(lst) - 1):
        left = lst[i - 1]
        middle = lst[i]
        right = lst[i + 1]

        
        if not ((middle > left and middle > right) or (middle < left and middle < right)):
            return False

    return True


print(is_zigzag([1, 3, 2, 4, 3]))   
print(is_zigzag([1, 4, 2, 5, 3]))   