# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n
    length = 1
    direction = 0
    for i in range(1, n):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break 
        step = 1 if diff > 0 else -1
        if direction == 0:
            direction = step
            length += 1
        elif step == -direction:
            direction = step
            length += 1
        else:
            break
    return length

def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    if n == 0:
        return []
    if n == 1:
        return [1]

    def from_start(i):
        length = 1
        direction = 0  
        for j in range(i + 1, n):
            diff = lst[j] - lst[j - 1]
            if diff == 0:
                break
            step = 1 if diff > 0 else -1
            if direction == 0:
                direction = step
                length += 1
            elif step == -direction:
                direction = step
                length += 1
            else:
                break
        return length

    return [from_start(i) for i in range(n)]





