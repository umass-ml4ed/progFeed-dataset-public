# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if len(lst) < 3:
        return True
    for i in range(1, len(lst) - 1):
        if not ((lst[i] > lst[i - 1] and lst[i] > lst[i + 1]) or (lst[i] < lst[i - 1] and lst[i] < lst[i + 1])):
            return False
    return True

assert is_zigzag([1, 3, 2, 4, 3]) is True
assert is_zigzag([1, 4, 2, 5, 3]) is True
assert is_zigzag([1, 2, 3, 4]) is False
assert is_zigzag([10]) is True
assert is_zigzag([1, 3, 2, 4, 5]) is False

assert is_zigzag([]) is True
assert is_zigzag([1, 2]) is True
assert is_zigzag([2, 1, 2, 1, 2]) is True
assert is_zigzag([2, 2, 2]) is False
assert is_zigzag([3, 1, 2]) is False