#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def max_recursive(lst): 
    if len(lst) == 0: 
        return 0 
    if len(lst) == 1: 
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]))    # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([8, 6]))           # returns 8
print(max_recursive([6]))              # returns 6 -> base case
print(max_recursive([]))               # returns 0 -> base case

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2: 
        return 0 
    next_value = sum_lists_recursive(lst1[1:], lst2[1:])
    return lst1[0] + lst2[0] + next_value

print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
print(sum_lists_recursive([3], [6]))             # returns 9
print(sum_lists_recursive([],[]))                # returns 0 -> base case

def funky(n):
    if n == 0 or n == 1: 
        return 1 
    elif n % 2 == 0: 
        return 2 * funky(n//2)
    else:
       return 1 + 2 * funky(n +1)

print(funky(2))
print(funky(10))
print(funky(50))
print(funky(-10))
print(funky(-50))
