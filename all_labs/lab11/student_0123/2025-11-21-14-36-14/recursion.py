# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)

print(max_recursive([3, 10, 2, 8, 6]))
print(max_recursive([10, 2, 8, 6]))
print(max_recursive([6]))
print(max_recursive([]))
#print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
#print(sum_lists_recursive([3], [6]))
#print(sum_lists_recursive([],[]))
#print(funky(2))
#print(funky(10))
#print(funky(50))