# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    cnt=0
    i=1
    if(len(lst)<2):
        return len(lst)
    else:
        for i in range (1, len(lst)-1):
            if((lst[i-1]>lst[i] and lst[i+1]>lst[cnt]) or lst[i-1]<lst[i] and lst[i+1]<lst[i]):
                cnt+=1
        return cnt+2

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag

print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)

print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start

print(longest_zigzag_from_start([10]))  # 1 → single element

print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start
