# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    if len(lst) >= 2:
        if lst[0] >= lst[1]:
            lst.pop(1)
            return max_recursive(lst)
        elif lst[0] < lst[1]:
            lst.pop(0)
            return max_recursive(lst)

def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))

print(sum_lists_recursive([], []))
def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n + 1)
