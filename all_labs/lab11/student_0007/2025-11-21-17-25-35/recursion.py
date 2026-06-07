# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    m = max_recursive(nums[1:])
    
    if nums[0] > m:
        return nums[0]
    return m


def sum_lists_recursive(a, b):
    if len(a) == 0:
        return 0
    
    first_sum = a[0] + b[0]
    rest_sum = sum_lists_recursive(a[1:], b[1:])
    
    return first_sum + rest_sum


def funky(n):
    if n == 0 or n == 1:
        return 1
    
    if n % 2 == 0:
        return 2 * funky(n // 2)
    
    return 1 + 2 * funky(n + 1)


def permutations(lis):
    if len(lis) == 1:
        return [lis[:]]
    result = []
    for i in range(len(lis)):
        front = lis[i]
        remaining = lis[:i] + lis[i+1:]
        for p in permutations(remaining):
            result.append([front] + p)
    return result

