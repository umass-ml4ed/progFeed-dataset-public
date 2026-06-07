# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(nums):

    if len(nums) < 3:
        return True

  
    for i in range(1, len(nums) - 1):
        left = nums[i - 1]
        middle = nums[i]
        right = nums[i + 1]

       
        if not ((middle > left and middle > right) or (middle < left and middle < right)):
            return False

    return True





        