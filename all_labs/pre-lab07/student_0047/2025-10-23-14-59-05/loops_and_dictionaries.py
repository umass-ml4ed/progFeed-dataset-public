# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result=""
    for num in range (n,0):
        for numb in range (num,0):
            result+=str(numb)+" "
        result+="\n"
    return result
        


def merge_dicts(d1,d2):
    for element in d2:
        if element in d1:
            d1[element]+=d2[element]
        else:
         d1[element]=d2[element]
    return d1




