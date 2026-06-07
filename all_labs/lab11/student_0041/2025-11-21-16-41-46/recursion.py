# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if(lst == []):
        return 0
    
    count = lst[0]
    rest = max_recursive(lst[1::])

    if(count < rest):
        count = rest

    return count # do not return recur. at the end bc that would add

print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([]))               # returns 0 -> base case

def sum_lists_recursive(lst1, lst2):
    if(lst1 == [] and lst2 == []):
        return 0
    
    last_digit = lst1[0]
    rest = lst1[1::]

    last_digit2 = lst2[0]
    rest2 = lst2[1::]

    lst1_sum = last_digit + sum_lists_recursive(rest, rest2) # lwk, ask how that worked bc i guessed
    lst2_sum = last_digit2

    return lst1_sum + lst2_sum

print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16


def funky(n):
    if(n == 0 or n == 1):
        return 1 # base case
    # no need for funky() since it doesn't have a variable to return, thus making it a base case

    if(n%2 == 0):
        return 2*funky(n//2) # f(n) is essen. funky(n) as funky is the "function", like f
    else:
        return 1+2*funky(n+1)

print(funky(2))
print(funky(10))