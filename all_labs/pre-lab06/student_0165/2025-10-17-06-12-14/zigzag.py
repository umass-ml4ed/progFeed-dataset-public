# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

"""
Take a list of integers lst as a parameter
Return the length of the longest zigzag subsequence that starts from the first element
The subsequence must start at index 0 and include consecutive elements
A list of fewer than 2 elements counts as a zigzag of length equal to the list length
"""
def longest_zigzag_from_start(lst):

    length = 1
    direction = 0 

    if len(lst) < 2:
        return len(lst)
    
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            if direction != 1:
                length += 1
                direction = 1
            else:
                break
        elif lst[i] < lst[i - 1]:
            if direction != -1:
                length += 1
                direction = -1
            else:
                break
        else:
            break
    return length


