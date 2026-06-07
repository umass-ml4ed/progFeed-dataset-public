# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) <= 1:
        return len(lst)
    a = lst[1] - lst[0]     
    if a == 0:
        return 1
    count = 2
    for i in range(2, len(lst)):
        b = lst[i] - lst[i-1]
        if b == 0:
            break
        if (a * b) < 0:
            count += 1
            a = b
        else:
            break
    return count



def zigzag_lengths_from_all_starts(lst):
    r = []

    for i in range(len(lst)):
        if i == len(lst) - 1:
            r.append(1)
            continue
        a = lst[i + 1] - lst[i]
        if a == 0:
            r.append(1)
            continue
        count = 2
        for j in range(i + 2, len(lst)):
            b = lst[j] - lst[j - 1]
            if b == 0:
                break
            if (a * b) < 0:
                count += 1
                a = b
            else:
                break
        r.append(count)
    return r
            




