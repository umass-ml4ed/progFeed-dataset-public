# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst:list):
    longest=2
    zigzag=2
    if len(lst)<=2:
        return len(lst)
    for i in range(1,len(lst)-1):
        if (int(lst[i])>int(lst[i-1]) and int(lst[i])>int(lst[i+1])) or  (int(lst[i])<int(lst[i-1]) and int(lst[i])<int(lst[i+1])):
            zigzag+=1
        else:
            zigzag=2
        longest=max(longest,zigzag)
            
    return longest

#rint(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag

#print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)

#print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start

#print(longest_zigzag_from_start([10]))  # 1 → single element

#print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start

def zigzag_lengths_from_all_starts(lst:list):
    length=len(lst)
    starts=[0]*length

    for i in range(length):
        zigzag=1
        last=0
        for j in range(i+1,length):
            difference=lst[j]-lst[j-1]
            if difference==0:
                break
            if last==0 or difference*last<0:
                zigzag+=1
                last=difference
            else:
                break
        starts[i]=zigzag
    
            
    return starts

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]
