# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    count=0
    if (len(list)<3):
        return True
    else:
        for num in range(list[1],list[len(list)-1]):
            if ((num>list[count] and num>list[count+2])  or (num<list[count] and num<list[count+2])):
                count+=1
            else:
                return False
    
    return True





