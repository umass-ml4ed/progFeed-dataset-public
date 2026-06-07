# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

lst = [2, 4, 3, 9, 14, 8]
def max_recursive(lst):
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_recursive(lst[1:]))
    
print(max_recursive(lst))
    
lst1 = 1, 2, 3
lst2 = 4, 5, 6
def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

print(sum_lists_recursive(lst1, lst2))

def funky(n):
    if n == 0 or n ==1:
        return 1
    if n%2 == 0:
        return 2 * funky(n//2)
    else:
        return 1+2*funky(n+1)
    
print(funky(50))