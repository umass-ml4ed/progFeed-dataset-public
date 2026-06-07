# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def max_recursive(lst):
  if len(lst) == 1:
    return lst[0]
  
  remaining = max_recursive(lst[1:])
  if lst[0] > remaining:
    return lst[0]
  else:
    return remaining



def sum_lists_recursive(lst1, lst2):
  
  if not (len(lst1) and len(lst2)):
    return 0
  
  remaining = sum_lists_recursive(lst1[1:], lst2[1:])
  
  res = lst1[0] + lst2[0] + remaining

  return res
  

print(sum_lists_recursive([1,2,3],[4,5,6]))


def funky(n):
  if n == 1 or n == 0:
    return 1
  elif n%2 == 0:
    return 2*funky(n//2)
  else:
    return 1+(2*funky(n+1))
  
def permutations(lst):
  if len(lst) == 0:
    return [[]]
  result = []
  first = lst[0]
  rest = permutations(lst[1:])
  for r in rest:
    for i in range(len(r) + 1):
      result.append(r[:i] + [first] + r[i:])
  return result
