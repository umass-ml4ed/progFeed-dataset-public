# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

from typing import List, Any


def max_recursive(lst: List[float]) -> float:
    if not lst:  
        return 0
    if len(lst) == 1:  
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max



def sum_lists_recursive(lst1: List[float], lst2: List[float]) -> float:
    if not lst1 and not lst2:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])



def funky(n: int) -> int:
    raise NotImplementedError("Please provide the mathematical recursive definition of funky(n).")


def permutations(lis: List[Any]) -> List[List[Any]]:
    if len(lis) == 1:
        return [lis[:]] 
    retlis: List[List[Any]] = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms_of_remaining = permutations(remaining)
        for p in perms_of_remaining:
            retlis.append([front_item] + p)
    return retlis
