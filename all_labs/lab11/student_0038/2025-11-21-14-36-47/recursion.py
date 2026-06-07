# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def sum_lists_recusive(lst1, lst2):
    lst_sum = 0
    lst_sum += lst1[0] + lst2[0]
    lst1.pop(0)
    lst2.pop(0)
    sum_lists_recusive(lst1, lst2)
    return lst_sum

print(sum_lists_recusive([1, 2, 3], [4, 5, 6]))
    

    