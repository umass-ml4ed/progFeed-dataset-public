# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

"""
def is_zigzag(lst):
    if len(lst) < 3:
        return True
    for i in lst:
        if lst.index(i) == 0:
            continue
        if lst.index(i) == (len(lst) - 1):
            break
        previous = lst[lst.index(i)-1]
        next = lst[lst.index(i) + 1]
        if (i < previous and i < next) or (i > previous and i > next):
            continue
        return False
    return True
"""

#print(is_zigzag([1, 3, 2, 4, 3]))
#print(is_zigzag([1, 4, 2, 5, 3]))
#print(is_zigzag([1, 2, 3, 4]))
#print(is_zigzag([10]))
#print(is_zigzag([1, 3, 2, 4, 5]))

def longest_zigzag_from_start(lst):
    count = 2 # for first and last items, which are not checked but always count
    if len(lst) < 2:
        return len(lst)
    for index, item in enumerate(lst):
        if index == 0: # skip first item
            continue
        if index == len(lst) - 1:
            break
        previous = lst[index - 1]
        next = lst[index + 1]
        if (item < previous and item < next) or (item > previous and item > next):
            count += 1
        else:
            break
    return count

#print(longest_zigzag_from_start([1,3,2,4,3,5])) # 6
#print(longest_zigzag_from_start([1,3,2,4,3])) # 5
#print(longest_zigzag_from_start([1,3,2,4,5,6,7])) # 4
#print(longest_zigzag_from_start([1,3,2,4,3,3,3])) # 5
#print(longest_zigzag_from_start([0])) # 1
#print(longest_zigzag_from_start([0,1])) # 2
#print(longest_zigzag_from_start([0,1, 2])) # 2

def zigzag_lengths_from_all_starts(lst):
    result = []
    for index, item in enumerate(lst):
        newlst = lst[index:]
        result.append(longest_zigzag_from_start(newlst))
    return result

#print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]
#print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]
#print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]
#print(zigzag_lengths_from_all_starts([10]))  # [1]

