# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    
    if len(lst) == 1:
        return lst[0]
    
    return max(lst[0], max_recursive(lst[1:]))

print(max_recursive([3, 10, 2, 8, 6]))
print(max_recursive([15, 1, 4, 9]))
print(max_recursive([5, 2, 8, 12]))
print(max_recursive([7]))

def sum_lists_recursive(lst1, lst2):
    if not lst1:
        return 0
    
    return (lst1[0] + lst2[0]) + sum_lists_recursive(lst1[1:], lst2[1:])

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
print(sum_lists_recursive([10, 20], [1, 2]))
print(sum_lists_recursive([1,2],[3,4]))

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)
    
print(funky(100))
print(funky(10))
print(funky(4))

