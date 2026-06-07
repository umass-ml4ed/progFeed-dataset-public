# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def max_recursive(n):
    if n == []: #base case 1, checks if the list is empty
        return 0
    if len(n) == 1: #we know that this element is the biggest in the list
        return n[0]
    first_val = n[0] 
    rest_val = n[1:]
    rest_max = max_recursive(rest_val)
    if first_val > rest_max:
        return first_val
    else:
        return rest_max
lst = [1, 2, 3, 12, 423, 32, 3]   
print(max_recursive(lst))

def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0
    sum1 = lst1[0] + lst2[0]
    rest_lst1 = lst1[1:]
    rest_lst2 = lst2[1:]
    sum2 = sum_lists_recursive(rest_lst1, rest_lst2)
    new_sum = sum2 + sum1
    return new_sum

lst = [1, 2, 3]
lststa = [4, 5, 6]
print(sum_lists_recursive(lst, lststa))

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n + 1)
print(funky(10))
print(funky(50))
print(funky(-10))
print(funky(-50))