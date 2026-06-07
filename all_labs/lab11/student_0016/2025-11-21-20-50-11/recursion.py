# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]
    targ = max_recursive(lst[1:])
    if targ > lst[0]:
        return targ
    else:
        return lst[0]
    
def sum_lists_recursive(lst1, lst2):
    if lst1 == []:
        return 0
    sum = sum_lists_recursive(lst1[1:], lst2[1:])
    return sum + lst1[0] + lst2[0]

def funky(n):
    if n == 0 or n == 1:
        return 1
    if (n % 2) == 0:
        return (2 * funky(n // 2))
    else:
        return (1 + (2 * funky(n + 1)))
    
def permutations(lis):
    if len(lis) == 1:
        return [lis]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i + 1:]
        n = permutations(remaining)
        for returned_permu in n:
            a = [front_item] + returned_permu
            retlis.append(a)
    return retlis