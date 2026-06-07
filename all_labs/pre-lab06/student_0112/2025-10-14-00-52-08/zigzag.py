# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def is_zigzag(lst):
        if len(lst) < 3 : 
            return True
        else:
            for i in range (1,len(lst)-1):
                if not ((lst[i] > lst[i+1] and lst[i] > lst[i-1]) or (lst[i] < lst[i+1] and lst[i] < lst[i-1])):
                    return False
                i+=1
            return True
def longest_zigzag_from_start(lst):
    count = 0
    if len(lst) < 3: 
         count = len(lst)
    else:
        check_lst =[]
        for i in range (len(lst)):
            check_lst.append(lst[i])
            if (is_zigzag(check_lst)):
                count += 1
    return count
def zigzag_lengths_from_all_starts(lst):
    new_list = []
    for i in range (len(lst)):
        check_lst =[]
        count = 0
        for j in range (i, len(lst)):
            check_lst.append(lst[j])
            if (is_zigzag(check_lst)):
                count += 1
        new_list.append(count)
    return new_list

        


          
     