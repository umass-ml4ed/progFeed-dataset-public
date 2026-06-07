# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(l):
    if not l:
        return 0
    if len(l)==1:
        return l[0]
    sub_max = max_recursive(l[1:])
    return l[0] if l[0] > sub_max else sub_max

def sum_lists_recursive(l1, l2):
    if not l1 and not l2:
        return 0
    return l1[0] + l2[0] + sum_lists_recursive(l1[1:], l2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    return 1 + 2 * funky(n + 1)

