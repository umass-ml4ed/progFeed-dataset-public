# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst)<2:
        return len(lst)

    D=lst[1]-lst[0]
    if D==0:
        return 1

    length = 2
    for i in range(2, len(lst)):
        diff=lst[i] - lst[i - 1]
        if diff==0:
            break
        if diff*D<0:
            length+=1
            D=diff
        else:
            break
    return length

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))
print(longest_zigzag_from_start([10]))
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))

def zigzag_lengths_from_all_starts(lst):
    if len(lst)<2:
        return [len(lst)]
    result=[]
    for i in range(len(lst)):
        if i==len(lst)-1:
            result.append(1)
            continue
  
        D=lst[i+1]-lst[i]
        if D==0:
            result.append(1)
            continue

        length=2
        for j in range(i+2,len(lst)):
            diff=lst[j]-lst[j-1]
            if diff==0:
                break
            if diff*D<0:
                length+=1
                D=diff
            else:
                break
        result.append(length)
    return result
print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))
print(zigzag_lengths_from_all_starts([10]))