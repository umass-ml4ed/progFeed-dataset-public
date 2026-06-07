# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst)->int:
    count = 1
    last_direction = 0

    for i in range(1,len(lst)):
        diff = lst[i]-lst[i-1]
        if(diff>0):
            if last_direction<=0:
                last_direction =1 
                count+=1
            else:
                break
        elif(diff<0):
            if last_direction>=0:
                last_direction = -1
                count+=1
            else:
                break
        else:
            break
    return count

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))
print(longest_zigzag_from_start([10]))
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))



def zigzag_lengths_from_all_starts(lst):
    
    result =[]
    for i in range(0,len(lst)):
        count = 1
        last_direction = 0
        for j in range(i+1,len(lst)):
            diff = lst[j]-lst[j-1]
            if(diff>0):
                if last_direction<=0:
                    last_direction = 1 
                    count+=1
                else:
                    result.append(count)
                    break
            elif(diff<0):
                if last_direction>=0:
                    last_direction = -1
                    count+=1
            else:
                break  
        result.append(count)

    return result


print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))
print(zigzag_lengths_from_all_starts([10]))


