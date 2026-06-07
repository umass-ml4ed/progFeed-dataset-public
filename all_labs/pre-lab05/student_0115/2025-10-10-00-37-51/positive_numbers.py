# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(nums):
    result=[]
    for n in nums:
        if n>0:
            result.append(n)
    return result

print(filter_positive([1, -3, 5, 0, -2, 7]))
print(filter_positive([-5, -1, -10]))
print(filter_positive([10, 20, -30, 40]))
