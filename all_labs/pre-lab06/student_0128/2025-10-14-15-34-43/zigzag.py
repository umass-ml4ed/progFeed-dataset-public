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