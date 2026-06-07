def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max


def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Even case
    if n % 2 == 0:
        return 2 * funky(n // 2)
    
    # Odd case
    return 1 + 2 * funky(n + 1)



def permutations(lis):
    # Base case: only one item -> only one permutation (a list containing that list)
    if len(lis) == 1:
        return [lis[:]]  # return a new list containing a copy of lis

    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        # remaining items: everything except index i
        remaining = lis[:i] + lis[i+1:]
        # get all permutations of the remaining items
        perms_of_remaining = permutations(remaining)
        # prepend front_item to each permutation of the remaining
        for p in perms_of_remaining:
            retlis.append([front_item] + p)

    return retlis



