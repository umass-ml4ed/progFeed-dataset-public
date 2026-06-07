# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def longest_zigzag_from_start(lst):
    evil_not_zigzag_perchance = len(lst) - 1
    for i in range(1, len(lst) - 1):
        if not ((lst[i] > lst[i + 1] and lst[i] > lst[i - 1]) or (lst[i] < lst[i + 1] and lst[i] < lst[i - 1])):
            evil_not_zigzag_perchance = i
            break
    return evil_not_zigzag_perchance + 1

def zigzag_lengths_from_all_starts(lst):
    cooler_list = []
    a_list = []
    while len(lst) > 2:
        if len(lst) == longest_zigzag_from_start(lst):
            for a in range(1, len(lst) + 1):
                a_list.append(a)
            a_list.reverse()
            cooler_list.extend(a_list)
            break
        for i in range(1, len(lst) - 1):
            if not ((lst[i] > lst[i + 1] and lst[i] > lst[i - 1]) or (lst[i] < lst[i + 1] and lst[i] < lst[i - 1])):
                cooler_list.append(i + 1)
                break
        lst.pop(0)
    if len(lst) == 2:
        cooler_list.append(2)
        lst.pop(0)
    if len(lst) == 1:
        cooler_list.append(1)
    return cooler_list