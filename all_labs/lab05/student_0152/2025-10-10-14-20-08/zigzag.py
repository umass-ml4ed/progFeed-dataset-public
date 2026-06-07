# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) < 3:
        return True
    for i in range(1, (len(list) - 1)):
        if not ((list[i] > list[i - 1] and list[i] > list[i + 1]) or
                (list[i] < list[i - 1] and list[i] < list[i + 1])):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))
print(is_zigzag([1, 4, 2, 5, 3]))
print(is_zigzag([1, 2, 3, 4]))
print(is_zigzag([10]))
print(is_zigzag([1, 3, 2, 4, 5]))