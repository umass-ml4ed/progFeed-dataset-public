# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result=""
    for num in range (n,0,-1):
        line=""
        for numb in range (num,0,-1):
            line+=str(numb)+" "

        result+=line+"\n"
    return result
print(pyramid(5))


def merge_dicts(d1,d2):
    for element in d2:
        if element in d1:
            d1[element]+=d2[element]
        else:
         d1[element]=d2[element]
    return d1




