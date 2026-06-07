# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst:list):
    if len(lst) == 0:
        return 0 
    elif len(lst) == 1:
        return lst[0]
    else:
        compare = max_recursive(lst[1:])
        return lst[0] if lst[0] > compare else compare

print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]) )   # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([8, 6]))           # returns 8
print(max_recursive([6]))              # returns 6 -> base case
print(max_recursive([]))               # returns 0 -> base 

def sum_lists_recursive(lst1:list, lst2:list):
    if len(lst1) == 0:
        return 0
    return lst1[-1] + lst2[-1] + sum_lists_recursive(lst1[:-1], lst2[:-1])

print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
print(sum_lists_recursive([3], [6]))             # returns 9
print(sum_lists_recursive([],[]))                # returns 0 -> base case

def funky(n:int):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)
    
print(funky(2))#2 
print(funky(10))#=74
print(funky(50))#=554
print(funky(-10))#=50
print(funky(-50))#=418