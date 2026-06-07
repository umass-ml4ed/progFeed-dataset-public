# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    
    if len(lst) == 1:
        return lst[0]
    
    rest_max = max_recursive(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max
    
def sum_lists_recursive(lst1, lst2):
    # base case: both empty
    if len(lst1) == 0:
        return 0
    
    # recursive case: first pair + sum of rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    # example structure only — fill in from the formula in your handout!

    # base case(s)
    if n == 0:
        # return the base value from the definition
        return 0   # <- this is just a placeholder

    # positive side recursive rule
    if n > 0:
        # use the recurrence for positive n, e.g.:
        # return funky(n - 1) + something_with(n)
        return funky(n - 1)  # <- replace with correct formula

    # negative side recursive rule
    else:  # n < 0
        # use the recurrence for negative n, e.g.:
        # return funky(n + 1) + something_with(n)
        return funky(n + 1)  # <- replace with correct formula


