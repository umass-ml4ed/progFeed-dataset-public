# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(nums:list):
    
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    
    sub_interval = max_recursive(nums[1:])
    
    if nums[0] > sub_interval:
        return nums[0]
    else:
        return sub_interval
    
