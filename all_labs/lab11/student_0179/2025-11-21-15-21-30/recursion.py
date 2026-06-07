# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) < 1:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        n = max_recursive(lst[1:])
        if lst[0] > n:
            n = lst[0]
            return n
        else:
            return n

print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]))    # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([8, 6]))           # returns 8
print(max_recursive([6]))              # returns 6 -> base case
print(max_recursive([]))               # returns 0 -> base case
print(max_recursive([3.2,3.1,3.3]))

def sum_lists_recursive(lst1, lst2):
    i = 0
    if len(lst1[i:]) < 1:
        return 0
    return lst1[i] + lst2[i] + sum_lists_recursive(lst1[i + 1:],lst2[i + 1:])

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
print(sum_lists_recursive([2, 3], [5, 6]))
print(sum_lists_recursive([3],[6]))
print(sum_lists_recursive([],[]))

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)
    
print(funky(2))
print(funky(10))
print(funky(50))
print(funky(-10))
print(funky(-50))

