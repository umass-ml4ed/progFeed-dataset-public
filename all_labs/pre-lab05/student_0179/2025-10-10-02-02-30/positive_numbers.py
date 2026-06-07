# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(nums):
    positive_nums = []
    for num in nums:
        if num > 0:
            positive_nums.append(num)
    return positive_nums

#print(filter_positive([1, -3, 5, 0, -2, 7]))
#print(filter_positive([-5, -1, -10]))
#print(filter_positive([10, 20, -30, 40]))