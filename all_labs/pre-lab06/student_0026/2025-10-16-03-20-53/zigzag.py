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

def zigzag_lengths_from_all_starts(lst):
    lengths=[]
    if len(lst)<2:
        return [len(lst)]
    for number in range(len(lst)):
        if number == len(lst)-1:
            lengths.append(1)
            continue
        difference1=lst[number+1]-lst[number]
        if difference1==0:
            lengths.append(1)
            continue
        zigzagcount=2
        for i in range(number+2, len(lst)):
            difference2=lst[i]-lst[i-1]
            if difference2==0:
                break
            if (difference1>0 and difference2<0) or (difference1<0 and difference2>0):
                zigzagcount+=1
                difference1=difference2
            else:
                break
        lengths.append(zigzagcount)
    return lengths

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]


