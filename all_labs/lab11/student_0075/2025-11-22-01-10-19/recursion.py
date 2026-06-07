# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    max = max_recursive(lst[1:])
    return lst[0] if lst[0] > max else max

print(max_recursive([2,5,5,4,3,2,7,9]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0

    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

print(sum_lists_recursive([1,2,3],[4,5,6]))

def funky(n):
    if n == 0:
        return 0
    if n > 0:
        return n + funky(n - 1)
    else:
        return -n + funky(n + 1)
    
print(funky(0))

print(funky(0))
print(funky(1))
print(funky(2))
print(funky(3))
print(funky(4))
print(funky(5))
print(funky(10))
print(funky(-1))
print(funky(-2))
print(funky(-3))
