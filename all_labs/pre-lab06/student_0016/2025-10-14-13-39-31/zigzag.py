# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    else:
        index = 1
        counter = 2
        for number in lst[1:-1]:
            if (number < lst[index - 1] and number < lst[index + 1]) or (number > lst[index - 1] and number > lst[index + 1]):
                counter += 1
            else:
                break
            index += 1
        return counter

def zigzag_lengths_from_all_starts(lst):
    zigzag_lst = []
    if len(lst) < 2:
        zigzag_lst.append(len(lst))
        return zigzag_lst
    else:
        index = 0
        for number in lst[0:-1]:
            in_index = index + 1
            counter = 2
            for number in lst[(index + 1):-1]:
                if (number < lst[in_index - 1] and number < lst[in_index + 1]) or (number > lst[in_index - 1] and number > lst[in_index + 1]):
                    counter += 1
                else:
                    break
                in_index += 1
            index += 1
            zigzag_lst.append(counter)
        zigzag_lst.append(1)
        return zigzag_lst
                
# I might be stupid this took concerningly long