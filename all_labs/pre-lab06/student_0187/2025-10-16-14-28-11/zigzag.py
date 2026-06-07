# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1
    i = 1
    prev = lst[1] - lst[0]
    
    if prev != 0:
        length = 2

    while i < len(lst) - 1 and prev != 0:
        diff = lst[i + 1] - lst[i]
        if diff != 0 and ((prev > 0 and diff < 0) or (prev < 0 and diff > 0)):
            length += 1
            prev = diff
        else:
            prev = 0 
        i += 1

    return length

def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    result = []

    for i in range(n):
        length = 1
        if i < n - 1:
            prev = lst[i + 1] - lst[i]
            if prev != 0:
                length = 2
            j = i + 1
            while (j < n - 1) and (prev != 0):
                diff = lst[j + 1] - lst[j]
                if diff != 0 and ((prev > 0 and diff < 0) or (prev < 0 and diff > 0)):
                    length += 1
                    prev = diff
                else:
                    prev = 0  
                j += 1
        result.append(length)

    return result

#    print(longest_zigzag_from_start([1, 3, 2, 4, 3]))       
#   print(longest_zigzag_from_start([1, 2, 3, 4, 5]))       
#    print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))     
#    print(longest_zigzag_from_start([10]))                   
#    print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  

#    print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))        
#    print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))        
#    print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))     
 #   print(zigzag_lengths_from_all_starts([10]))                   

