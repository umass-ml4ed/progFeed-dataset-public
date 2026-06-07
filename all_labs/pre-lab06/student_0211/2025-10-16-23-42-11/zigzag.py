# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#def longest_zigzag_from_start(lst: list):


# def longest_zigzag_from_start(lst: list):
#     ziglen = 0
#     if len(lst) < 2:
#        ziglen = len(lst)
#     a = 1
#     while(a < len(lst)):
#         for i in lst:
#             if (lst[a] > i and lst[a]> lst[a+1]) or (lst[a] > i and lst[a]> lst[a+1]):
#                 ziglen = len(range(a+2))
#             a +=1 
#     return ziglen

# print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag
def longest_zigzag_from_start(lst: list):

    if len(lst) < 2:   # lists less than len 2
        return len(lst)

    lst2 = [lst[0],lst[1]]

    if lst[1]>lst[0]:   # direction at the start
        direction = "up"
    elif lst[1]<lst[0]:
        direction = "down" 
   
    for i in range(2,len(lst)):
            if lst[i] > lst[i-1] and direction == "down":
                 lst2.append(lst[i])
                 direction = "up"
            elif lst[i] < lst[i-1] and direction == "up":
                 lst2.append(lst[i])
                 direction = "down"
    return len(lst2)

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

