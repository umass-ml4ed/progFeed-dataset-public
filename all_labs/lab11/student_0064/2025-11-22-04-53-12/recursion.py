# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED

#bc and then compare it
def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]

    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

def sl_recursive(lst_1, lst_2):
    if len(lst_1) == 0:
        return 0
    return lst_1[0] + lst_2[0] + sl_recursive(lst_1[1:], lst_2[1:])

def funky(n):
    #the bc range
    if -2 <= n <= 2:
        return n

    if n > 2:
        return funky(n - 3) + n
    else:
        return funky(n + 3) + abs(n)
