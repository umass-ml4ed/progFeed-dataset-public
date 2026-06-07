# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    elif len(lst) == 1:
        return lst[0]
    elif (lst[0] > lst[1]):
        lst.remove(lst[1])
        max_recursive(lst)
    elif (lst[0] < lst[1]):
        lst.remove(lst[0])
        max_recursive(lst)

print(max_recursive([]))
print(max_recursive([8, 6]))
print(max_recursive([10, 2, 8, 6]))

def sum_lists_recursive(lst1, lst2):
    return "i'm working on it sorry"

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
print(sum_lists_recursive([2, 3], [4, 5]))
print(sum_lists_recursive([3], [6]))
print(sum_lists_recursive([], []))

def funky(n):
    if n == 1 or 0:
        n = 1
        return n
    elif n%2 == 0:
        n = 2 * funky(n//2)
        return n
    elif n%2 != 0:
        n = 1 + 2*funky(n+1)
        return n

print(funky(2))
print(funky(10))
print(funky(50))

#def permutations(lis):
    #extra credit, optional