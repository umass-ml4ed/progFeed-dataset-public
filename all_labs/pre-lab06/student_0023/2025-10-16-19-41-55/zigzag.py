# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n
    if lst[1] > lst[0]:
        direction = 'down'
    elif lst[1] < lst[0]:
        direction = 'up'
    else:
        return 1
    count = 2
    for i in range(1, n - 1):
        if direction == 'down' and lst[i] > lst[i + 1]:
            count += 1
            direction = 'up'
        elif direction == 'up' and lst[i] < lst[i + 1]:
            count += 1
            direction = 'down'
        else:
            break
    return count

def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    if n == 0:
        return []
    results = []
    for i in range(n):
        sublist = lst[i:]
        results.append(longest_zigzag_from_start(sublist))
    return results
