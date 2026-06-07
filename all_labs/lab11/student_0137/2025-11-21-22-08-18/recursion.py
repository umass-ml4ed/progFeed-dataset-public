# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    # Base case: empty list
    if lst == []:
        return 0

    if len(lst) == 1:
        return lst[0]

    rest_max = max_recursive(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max

def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n):
    if -2 <= n <= 2:
        return n

    if n > 2:
        return funky(n - 3) + 8

    return funky(n + 3) + 8

def permutations(lis):
    if len(lis) == 1:
        return [lis]

    result = []
    for i in range(len(lis)):
        front = lis[i]
        rest = lis[:i] + lis[i+1:]

        for p in permutations(rest):
            result.append([front] + p)

    return result