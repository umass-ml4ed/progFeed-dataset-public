# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

# Write a function, called longest_zigzag_from_start, which should:
# Take a list of integers lst as a parameter
# Return the length of the longest zigzag subsequence that starts from the first element
# The subsequence must start at index 0 and include consecutive elements
# A list of fewer than 2 elements counts as a zigzag of length equal to the list length

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n

    prev_dif = lst[1] - lst[0]
    if prev_dif == 0:
        return 1  

    length = 2  
    for i in range(2, n):
        dif = lst[i] - lst[i - 1]
        if dif == 0:
            break  
        if prev_dif * dif < 0:
            length += 1
            prev_dif = dif
        else:
            break
    return length


# Write a function, called zigzag_lengths_from_all_starts, which should:
# Take a list of integers lst as input
# Return a list of integers, where each element at index i is the length of the longest contiguous
# zigzag starting at position i
# Differences of 0 break the zigzag


def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    if n == 0:
        return []

    result = [1] * n 
    for start in range(n):
        if start == n - 1:
            result[start] = 1
            continue

        prev_dif = lst[start + 1] - lst[start]
        if prev_dif == 0:
            result[start] = 1
            continue

        length = 2
        for i in range(start + 2, n):
            dif = lst[i] - lst[i - 1]
            if dif == 0:
                break
            if prev_dif * dif < 0:
                length += 1
                prev_dif = dif
            else:
                break
        result[start] = length
    return result