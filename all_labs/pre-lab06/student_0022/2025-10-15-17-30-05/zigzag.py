# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    zig_zag_counter = 0
    if len(lst) < 2:
        return len(lst)
    else:
        for index in range(1, len(lst)-1):
            if ((lst[index-1] > lst[index] < lst[index+1]) or (lst[index-1] < lst[index] > lst[index+1])) and (lst[index-1] != lst[index+1]):
                zig_zag_counter += 1
    return zig_zag_counter+2

def zigzag_lengths_from_all_starts(lst):
    output_list = []
    for index in range(len(lst)):
        output_list.append(longest_zigzag_from_start(lst[index:]))
    return output_list
