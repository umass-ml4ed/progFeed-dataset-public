def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max


def sum_lists_recursive(lst,lst1):
    if len(lst)==0:
        return 0
    if len(lst1)==0:
        return 0
    res= sum_lists_recursive(lst[1:],lst1[1:])
    return lst[0]+lst1[0]+res

def funky(n):
    if n==0 or n==1:
        return 1
    elif n%2==0:
        return 2*funky(n//2)
    else:
        return 1+(2*funky(n+1))
    
    



