# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    first = lst[0]
    max_rest = max_recursive(lst[1:])
    return first if first >= max_rest else max_rest


def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n):

    raise NotImplementedError("funky()'s mathematical definition was not provided. Please supply it.")

def permutations(lis):
    if len(lis) == 1:
        return [lis[:]]

    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms_of_remaining = permutations(remaining)
        for perm in perms_of_remaining:
            retlis.append([front_item] + perm)
    return retlis
