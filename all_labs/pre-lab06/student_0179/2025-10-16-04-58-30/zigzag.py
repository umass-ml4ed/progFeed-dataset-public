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
        return len(new_lst)

def zigzag_lengths_from_all_starts(lst):
    total = []
    for i in range(0, len(lst)):
        count = 1
        for lsts in range(i, len(lst)-1):
            if lsts == i and lst[lsts] != lst[lsts + 1]:
                count += 1
            elif (lst[lsts] > lst[lsts - 1] and lst[lsts] > lst[lsts + 1]) or (lst[lsts] < lst[lsts - 1] and lst[lsts] < lst[lsts + 1]):
                count += 1
            else:
                break
        total.append(count)
    return total
