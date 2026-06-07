# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    count = 1
    for i in range(1, len(list) - 1):
        return((list[i] > list[i - 1] and list[i] > list[i + 1]) or (list[i] < list[i - 1] and list[i] < list[i + 1]))
    if count == len(list):
        return True
    else:
        return False
print(is_zigzag([1, 3, 2, 4, 3]))