# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def longest_zigzag_from_start(lst):
    l = 1
    if len(lst) < 2:
        return len(lst)
    for i in range(1, len(lst)):
        if lst[i] < 0 and lst[i-1] >= 0:
            l += 1
        elif lst[i] > 0 and lst[i-1] <= 0:
            l += 1
        else:
            break
    return l

#print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  
#print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  
#print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  
#print(longest_zigzag_from_start([10]))  
#print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))

def zigzag_lengths_from_all_starts(lst):
    l = 1
    lst_of_ints = []
    for i in range(1, len(lst)):
        if i == 1:
            if lst[i] < 0 and lst[i-1] >= 0:
                l += 1
        else:
            return l

    return lst_of_ints[l]




