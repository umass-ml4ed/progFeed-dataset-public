# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(numbers):
    if len(numbers) < 3:
        return True
    for i in range(1, len(numbers) - 1):
        left = numbers[i - 1]
        middle = numbers[i]
        right = numbers[i + 1]
        if not ((middle > left and middle > right) or (middle < left and middle < right)):
            return False 
        return True
print(is_zigzag([1, 3, 2, 4]))
