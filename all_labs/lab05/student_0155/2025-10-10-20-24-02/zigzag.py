# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if len(lst) < 3:
        return True
    for i in lst:
        if lst.index(i) == 0:
            continue
        if lst.index(i) == (len(lst) - 1):
            break
        previous = lst[lst.index(i)-1]
        next = lst[lst.index(i) + 1]
        if (i < previous and i < next) or (i > previous and i > next):
            continue
        return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))
print(is_zigzag([1, 4, 2, 5, 3]))
print(is_zigzag([1, 2, 3, 4]))
print(is_zigzag([10]))
print(is_zigzag([1, 3, 2, 4, 5]))