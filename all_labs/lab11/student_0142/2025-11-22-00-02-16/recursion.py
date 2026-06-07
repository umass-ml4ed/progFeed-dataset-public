# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max
    
max_recursive([3, 10, 2, 8, 6])
max_recursive([10, 2, 8, 6])

def sum_lists_recursive(lst1,lst2):
    if not lst1 and not lst2:
        return 0
    return lst1[0] +lst2[0]+ sum_lists_recursive(lst1[1:],lst2[1:])
    
from functools import lru_cache
@lru_cache(maxsize=None)
def funky(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:  # even
        return 2 * funky(n // 2)
    else:           # odd (and not 1)
        return 1 + 2 * funky(n + 1)

if __name__ == "__main__":
    tests = [2, 10, 50, -10, -50]
    for t in tests:
        print(f"funky({t}) = {funky(t)}")
