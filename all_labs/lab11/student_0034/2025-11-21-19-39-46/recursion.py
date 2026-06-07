# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def max_recursive(lst, max_num=0):  
    if len(lst) == 0:
        return 0
    if lst[0] > max_num:
        max_num = lst[0]
        lst.remove(lst[0])
    else:
        lst.remove(lst[0])
    return max_recursive(lst)


print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6]))    # returns 10
print(max_recursive([2, 8, 6]))        # returns 8
print(max_recursive([8, 6]))           # returns 8
print(max_recursive([6]))              # returns 6 -> base case
print(max_recursive([]))               # returns 0 -> base case


def sum_lists_recursive(lst1, lst2, total=0):
    if len(lst1) == 0:
        return 0
    total += lst1[0]
    lst1.remove(lst1[0])
    total += lst2[0]
    lst2.remove(lst2[0])
    return sum_lists_recursive(lst1, lst2)

# print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
# print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
# print(sum_lists_recursive([3], [6]))             # returns 9
# print(sum_lists_recursive([],[]))                # returns 0 -> base case


def funky(n):
    if n==0 or n==1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n + 1)

# print(funky(2))
# print(funky(10))
# print(funky(50))
# print(funky(-10))
# print(funky(-50))
