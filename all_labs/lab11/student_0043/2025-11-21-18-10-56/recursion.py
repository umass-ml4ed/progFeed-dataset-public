# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    x = max_recursive(lst[1:])
    if lst[0] > x:
        return lst[0]
    else:
        return x
    
    
def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0
    sum = lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
    return sum

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        return 2*funky(n//2)
    else:
        return 1 + 2 * funky(n+1)

def permutations(lis):
    # Base case
    if len(lis) == 1:
        return [lis]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms_of_remaining = permutations(remaining)
        for p in perms_of_remaining:
            retlis.append([front_item] + p)
    return retlis
print(permutations(['AA', 'BB', 'CC']))