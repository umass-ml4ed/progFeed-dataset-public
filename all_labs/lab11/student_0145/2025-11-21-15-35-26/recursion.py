# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
   
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]

   
    sub_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

def sum_lists_recursive(lst1, lst2):
    
    if not lst1:     
        return 0

    
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    """
    Recursive function defined by:
      f(n) = 1                     if n == 0 or n == 1
             2 * f(n//2)          if n is even
             1 + 2 * f(n+1)      otherwise (n odd)
    Works for positive and negative integers.
    """
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    return 1 + 2 * funky(n + 1)


if __name__ == "__main__":
    tests = [2, 10, 50, -10, -50]
    for t in tests:
        print(t, funky(t))  
