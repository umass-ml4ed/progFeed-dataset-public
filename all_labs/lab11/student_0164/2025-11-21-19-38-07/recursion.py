# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if not lst: 
        return None
    if len(lst) == 1:
        return lst[0]
    sub_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    val1 = lst1[0] if lst1 else 0
    val2 = lst2[0] if lst2 else 0
    return val1 + val2 + sum_lists_recursive(lst1[1:] if lst1 else [], lst2[1:] if lst2 else [])





def funky(n):
    if n < 1:
        raise ValueError("funky(n) not defined for n <= 0")
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2 * funky(n - 1) + 3 * funky(n - 2)



print(funky(0)) 
print(funky(2))

def permutations(lis):
    if not lis:                  # handle empty list
        return [[]]              # only permutation of empty list is empty list
    if len(lis) == 1:
        return [lis[:]]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        for perm in permutations(remaining):
            retlis.append([front_item] + perm)
    return retlis






    

