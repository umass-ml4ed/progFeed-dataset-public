# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(integers: list):
    if len(integers) < 3:
        return True
    for i in range(1, len(integers) - 1):
        if not ((integers[i] > integers[i-1] and integers[i] > integers[i+1]) or (integers[i] < integers[i-1] and integers[i] < integers[i+1])):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))