# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) <= 1:
        return len(lst)
    
    if lst[0] == lst[1]:
        return 1

    longer = 2
    n = 0 if lst[0] < lst[1] else 1 
    
    for w in range(1, len(lst)-1):
        diff = lst[w+1] - lst[w]
        
        if (n % 2 == 0 and diff < 0) or \
           (n % 2 != 0 and diff > 0):
            longer += 1
            n += 1
        else:
            return longer

    return longer

def zigzag_lengths_from_all_starts(lst):
    lengths = []
    for i in range(len(lst)):
        lengths.append(longest_zigzag_from_start(lst[i:]))
    return lengths

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))
print(zigzag_lengths_from_all_starts([10]))