# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1  # always count the first element
    prev_diff = 0  # no direction yet

    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]

        if diff == 0:
            break  # zeros break the zigzag
        
        if prev_diff == 0 or (diff > 0 and prev_diff < 0) or (diff < 0 and prev_diff > 0):
            length += 1
            prev_diff = diff
        else:
            break  # stop when it no longer alternates

    return length


def zigzag_lengths_from_all_starts(lst):
    output_list = []
    for index in range(len(lst)):
        output_list.append(longest_zigzag_from_start(lst[index:]))
    return output_list
