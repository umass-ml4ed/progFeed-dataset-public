# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    zz_length=2
    
    if len(lst)<2:
        zz_length=len(lst)
    else:
        
        for num in range(1,len(lst)-1):
      
            if (lst[num]>lst[num+1] and lst[num]>lst[num-1]) or (lst[num]<lst[num-1] and lst[num]<lst[num+1]) :
                zz_length+=1
            else: 
                 break
            

    return zz_length

def zigzag_lengths_from_all_starts(lst):
    newlst=lst
    result=[]
    if len(newlst)<=1:
        result.append(1)
    for num in range (0,len(lst)-1):
        result.append(longest_zigzag_from_start(newlst))
        newlst.pop(0)
        if len(newlst)==1:
            result.append(1)
    return result
        
        
print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]



