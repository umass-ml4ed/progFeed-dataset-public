# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_recursive(lst[1:]))

max_recursive([3, 10, 2, 8, 6]) # returns 10
max_recursive([10, 2, 8, 6])    # returns 10
max_recursive([2, 8, 6])        # returns 8
max_recursive([8, 6])           # returns 8
max_recursive([6])              # returns 6 

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

sum_lists_recursive([1, 2, 3], [4, 5, 6]) # returns 21
sum_lists_recursive([2, 3], [5, 6])       # returns 16
sum_lists_recursive([3], [6])             # returns 9
sum_lists_recursive([],[])                # returns 0 -> base case

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2*funky(n//2)
    if n % 2 != 0:
        return 1+2*funky(n+1)
    
print(funky(10))

