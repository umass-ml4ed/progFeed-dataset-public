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
    a=len(lst)
    if a==0:
        return []
    if a==1:
        return[1]
    for number in range(len(lst)):
        if number == a-1:
            lengths.append(1)
            continue
        difference0=lst[number]
        difference1=0
        for i in range(number+1, a):
            difference1=lst[i]-difference0
            if difference1!=0:
                break
            difference0=lst[i]
        if difference1==0: 
            lengths.append(1)
            continue
        zigzagcount=i-number+1
        difference2=difference1
        for b in range(i+1,a):
            difference3=lst[b]-lst[b-1]
            if difference3==0:
                break
            if (difference2>0 and difference3<0) or (difference2<0 and difference3>0):
                zigzagcount+=1
                difference2=difference3
            else:
                break
        lengths.append(zigzagcount)
    return lengths

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]


