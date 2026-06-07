# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) > 1:
        lst.sort()
        lst.pop(0)
        max_recursive(lst)
    return lst[0]

def sum_lists_recursive(lst1, lst2):
    if len(lst1) < 1 or len(lst2) < 1:
        return 0
    i = lst1.pop(0)
    j = lst2.pop(0)
    return i + j + sum_lists_recursive(lst1, lst2)


def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n+1)

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = front_item[:-1]
        permutations(remaining)
        for x in remaining:
            x += (front_item)
        retlis.append(remaining)
    return retlis

print(sum_lists_recursive([], []))
