# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1
    for i in range(1, len(lst)):
        if i == 1:
            if lst[i] != lst[i-1]:
                length += 1
                last_diff = lst[i] - lst[i-1]
            else:
                break
        else:
            diff = lst[i] - lst[i-1]
            if diff == 0:
                break
            if (diff > 0 and last_diff < 0) or (diff < 0 and last_diff > 0):
                length += 1
                last_diff = diff
            else:
                break
    return length


def zigzag_lengths_from_all_starts(lst):
    result = []
    for start in range(len(lst)):
        count = 1
        for i in range(start+1, len(lst)):
            if i == start+1:
                if lst[i] != lst[i-1]:
                    count += 1
                    last_diff = lst[i] - lst[i-1]
                else:
                    break
            else:
                diff = lst[i] - lst[i-1]
                if diff == 0:
                    break
                if (diff > 0 and last_diff < 0) or (diff < 0 and last_diff > 0):
                    count += 1
                    last_diff = diff
                else:
                    break
        result.append(count)
    return result