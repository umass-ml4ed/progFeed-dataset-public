# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if not lst: 
        return 0
    if len(lst) == 1:
        return lst[0]
    head = lst[0]
    tail_max = max_recursive(lst[1:])
    return head if head >= tail_max else tail_max



def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
  






def funky(n):
    if n == 0 or n == 1:
        return 1 
    if n % 2 == 0:
        return 2 * funky(n // 2)
    return 1 + 2 * funky(n + 1)



print(funky(2))
print(funky(0))
  










def permutations(lis):
    if len(lis) == 1:      
        return [lis[:]]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms_of_remaining = permutations(remaining)
        for p in perms_of_remaining:
            retlis.append([front_item] + p)
    return retlis








    

