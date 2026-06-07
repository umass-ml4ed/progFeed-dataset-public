# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(nums):
    
    n = len(nums)
    if n < 3:
        return True

    for i in range(1, n - 1): 
        left, mid, right = nums[i - 1], nums[i], nums[i + 1]
        if not ((mid > left and mid > right) or (mid < left and mid < right)):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))

