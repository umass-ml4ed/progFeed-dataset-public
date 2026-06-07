# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst)>1:
        longer = 1
        longest = 0
    else:
        return len(lst)
    
    n= 0 if lst[0]<lst[1] else 1
    
    for w in range(0,len(lst)-1):
        if lst[w+1]-lst[w]>0 if n%2==0 else lst[w+1]-lst[w]<0:
            longer+=1
            n+=1
        else:
            longest=(longer if longest < longer else longest)
            longer = 1
    return longer if longest < longer else longest

def zigzag_lengths_from_all_starts(lst):
    lengths = []
    for i in range(len(lst)):
        lengths.append(longest_zigzag_from_start(lst[i:]))
    return lengths

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]
