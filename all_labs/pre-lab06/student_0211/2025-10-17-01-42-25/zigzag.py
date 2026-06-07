# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def longest_zigzag_from_start(lst: list):

    if len(lst) < 2:   # lists less than len 2
        return len(lst)
    
    if lst[1] == lst[0]: # 1st and 2nd element are equal 
        return 1
    
    if lst[1] > lst [0]:
        direction = "up"
    else:
        direction = "down"
    
    length = 2
    zigzag = True 
    for i in range(2, len(lst)):
            if lst[i] > lst[i-1] and direction == "down":
                length += 1
                direction = "up"
            elif lst[i] < lst[i-1] and direction == "up":
                length += 1
                direction = "down"
            else:  
                return length
    return length
        


def zigzag_lengths_from_all_starts(lst: list):
    lst2 = []
    for i in range(len(lst)):
        length = longest_zigzag_from_start(lst[i:])
        lst2.append(length)
    return lst2


print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag

print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)

print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start

print(longest_zigzag_from_start([10]))  # 1 → single element

print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  

print(zigzag_lengths_from_all_starts([10]))

