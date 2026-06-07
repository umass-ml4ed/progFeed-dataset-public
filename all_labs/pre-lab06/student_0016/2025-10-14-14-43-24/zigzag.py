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
    if len(lst) == 1:
        zigzag_lst.append(len(lst))
        return zigzag_lst
    if len(lst) == 0:
        return zigzag_lst
    else:
        index_ahead = 1
        for number in lst[0:-1]:
            index = index_ahead
            counter = 2
            if number == lst[index_ahead]:
                    zigzag_lst.append(1)
                    continue
            for number in lst[(index_ahead):-1]:
                if (number < lst[index - 1] and number < lst[index + 1]) or (number > lst[index - 1] and number > lst[index + 1]):
                    counter += 1
                else:
                    break
                index += 1
            index_ahead += 1
            zigzag_lst.append(counter)
        zigzag_lst.append(1)
        return zigzag_lst
                
# I might be stupid this took concerningly long