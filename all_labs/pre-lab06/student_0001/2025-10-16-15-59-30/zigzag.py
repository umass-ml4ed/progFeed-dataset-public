# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1 
    increasing = None

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:  # increasing
            if increasing is None or increasing is False:
                length += 1
                increasing = True
            else:
                break

        elif lst[i] < lst[i - 1]:  # decreasing
            if increasing is None or increasing is True:
                length += 1
                increasing = False
            else:
                break
        else:
            continue

    return length


# print(longest_zigzag_from_start([1, 3, 2, 4, 3]))
# print(longest_zigzag_from_start([1, 2, 3, 4, 5]))
# print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))
# print(longest_zigzag_from_start([10]))
# print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))


def zigzag_lengths_from_all_starts(lst):
    result = []
    for i in range(len(lst)):
        sublist = lst[i:]
        length = longest_zigzag_from_start(sublist)
        result.append(length)
    return result

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))
print(zigzag_lengths_from_all_starts([10]))