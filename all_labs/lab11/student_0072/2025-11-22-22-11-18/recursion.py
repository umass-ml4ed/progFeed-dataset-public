def max_recursive(lst):
    if lst == []: 
        return 0
    elif len(lst) == 1:  
        return lst[0]
    else:
        head = lst[0]
        tail_max = max_recursive(lst[1:])
        return max(head, tail_max)

def sum_lists_recursive(lst1, lst2):
    if lst1 == []:
        return 0
    else:
        head_sum = lst1[0] + lst2[0]
        return head_sum + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)
