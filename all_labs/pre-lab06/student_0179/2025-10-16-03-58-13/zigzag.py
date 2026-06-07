# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    else:
        new_lst = [lst[0]]
        for lsts in range(1, len(lst)-1):
            new_lst.append(lst[lsts])
            if (lst[lsts] > lst[lsts - 1] and lst[lsts] > lst[lsts + 1]) or (lst[lsts] < lst[lsts - 1] and lst[lsts] < lst[lsts + 1]):
                continue
            else:
                break
        if new_lst == lst[0:len(lst)-1]:
            if (lst[len(lst)-2] > lst[len(lst)-3] and lst[len(lst)-2] > lst[len(lst)-1]) or (lst[len(lst)-2] < lst[len(lst)-3] and lst[len(lst)-2] < lst[len(lst)-1]):
                new_lst.append(lst[len(lst)-1])
        return new_lst
    
print(longest_zigzag_from_start([1, 3, 2, 4, 3]))
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))
print(longest_zigzag_from_start([10]))
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))