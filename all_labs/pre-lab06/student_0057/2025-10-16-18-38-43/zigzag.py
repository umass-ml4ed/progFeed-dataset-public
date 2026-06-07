# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(nums):
    if len(nums) < 3:
        return True
    for i in range(1, len(nums) - 1):
        left = nums[i - 1]
        right = nums[i + 1]
        middle = nums[i]
        if not ((middle > left and middle > right) or (middle < left and middle < right)):
            return False
    return True
print(is_zigzag([1, 3, 2, 4, 3]))
print(is_zigzag([1, 4, 2, 5, 3]))
print(is_zigzag([1, 2, 3, 4]))
print(is_zigzag([10]))
print(is_zigzag([1, 3, 2, 4, 5]))