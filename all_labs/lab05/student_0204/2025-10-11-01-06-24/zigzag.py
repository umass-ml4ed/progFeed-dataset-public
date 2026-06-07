# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) < 3:
        return True
    for x in range(1, len(list) - 1):
        if (list [x] > list[x + 1] and list[x] > list[x - 1]) or (list[x] < list[x - 1] and list[x] < list[x + 1]):
            continue
        else:
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True
print(is_zigzag([1, 4, 2, 5, 3]))    # True
print(is_zigzag([1, 2, 3, 4]))       # False
print(is_zigzag([1, 2, 1, 2]))
print(is_zigzag([10]))               # True
print(is_zigzag([1, 3, 2, 4, 5]))    # False
print(is_zigzag([]))