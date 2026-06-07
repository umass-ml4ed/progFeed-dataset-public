# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(nums):
    if len(nums) < 3:
        return True
    for i in range(1, len(nums) - 1):
        if not ((nums[i] > nums[i-1] and nums[i] > nums[i+1]) or
                (nums[i] < nums[i-1] and nums[i] < nums[i+1])):
            return False
    return True

