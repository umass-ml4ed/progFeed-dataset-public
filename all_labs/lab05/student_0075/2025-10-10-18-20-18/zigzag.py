# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(nums):
    if len(nums) < 3:
        return True
    for i in range(1, len(nums) - 1):
        a = nums[i-1]
        b = nums[i]
        c = nums[i+1]
        if not ((b > a and b > c) or (b < a and b < c)):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
