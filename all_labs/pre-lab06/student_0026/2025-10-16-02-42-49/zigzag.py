# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def longest_zigzag_from_start(lst):
    zigzagcount=0
    if len(lst)<2:
        zigzagcount=len(lst)
        return zigzagcount
    zigzagcount=2
    difference1= lst[1]-lst[0]
    for number in range(2, len(lst)):
        difference2=lst[number]-lst[number-1]
        if (difference2>0 and difference1<0) or (difference2<0 and difference1>0):
            zigzagcount+=1
            difference1=difference2 
        else:
            break
    return zigzagcount
        
print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag

print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)

print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start

print(longest_zigzag_from_start([10]))  # 1 → single element

print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start
