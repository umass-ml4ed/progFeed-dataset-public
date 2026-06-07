# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    sub_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])



def funky(n):
    if n == 0:
        return 1
    if n > 0:
        return n + funky(n - 2)
    return -n + funky(n + 2)


    
def permutations(lis):
    if len(lis) == 1:
        return [lis[:]]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        for perm in permutations(remaining):
            retlis.append([front_item] + perm)
    return retlis