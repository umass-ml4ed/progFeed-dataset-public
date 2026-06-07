def funky(n):
    if n == 1 or n == 0: return 1
    if n % 2 == 0:
        return funky(n // 2) * 2
    else:
        return 1 + funky(n + 1) * 2


def max_recursive(lst):
    if len(lst) == 0:
        return 0  # or raise an exception
    else:
        sub_max = max_recursive(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max
    
# def max_recursive(lst):
#     return max(lst) if len(lst) > 0 else 0  # or raise an exception

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    else:
        first_sum = lst1[0] + lst2[0]
        rest_sum = sum_lists_recursive(lst1[1:], lst2[1:])
        return first_sum + rest_sum

# def sum_lists_recursive(lst1, lst2):
#     return sum([a + b for a, b in zip(lst1, lst2)])

#the input is a list of any values
def permutations(lst):
    if len(lst) == 0:
        return [[]]
    else:
        result = []
        for i, char in enumerate(lst):
            for perm in permutations(lst[:i] + lst[i+1:]):
                result.append([char] + perm)
        return result

# # now implementing it without recursion
# def permutations(lst):
#     from itertools import permutations as it_permutations
#     return [list(p) for p in it_permutations(lst)]