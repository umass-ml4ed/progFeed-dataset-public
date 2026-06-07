# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    zig_zag_list = []
    if len(lst) == 1:
        return len(lst)
    else:
        for index in range(len(lst)-2):
            if ((lst[index] > lst[index+1] < lst[index+2]) or (lst[index] < lst[index+1] > lst[index+2])) and (lst[index] != lst[index+2]):
                zig_zag_list.append(lst[index+1])
    return len(zig_zag_list)+2

def zigzag_lengths_from_all_starts(lst):
    output_list = []
    for index in range(len(lst)):
        output_list.append(longest_zigzag_from_start(lst[index:]))
    return output_list
