# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    elif len(lst) == 1:
        return lst[0]
    new_case = lst[1: ]
    return max(lst[0], max_recursive(new_case))

print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]))    # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([8, 6]))           # returns 8
print(max_recursive([6]))              # returns 6 -> base case
print(max_recursive([]))               # returns 0 -> base case

def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0
    new_case1 = lst1[1: ]
    new_case2 = lst2[1: ]
    return lst1[0] + lst2[0] + sum_lists_recursive(new_case1, new_case2)

print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
print(sum_lists_recursive([3], [6]))             # returns 9
print(sum_lists_recursive([],[]))                # returns 0 -> base case

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)

print(funky(2)) #=2 
print(funky(10)) #=74
print(funky(50)) #=554
print(funky(-10)) #=50 
print(funky(-50)) #=418