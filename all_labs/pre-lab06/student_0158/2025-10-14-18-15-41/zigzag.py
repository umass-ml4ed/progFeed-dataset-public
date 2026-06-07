# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    z=0
    if len(lst)<2:
        return len(lst)
    else:
        for i in range(2, len(lst)):
            if (i-2)==0:
                if ((lst[i-1]-lst[i-2])>0) and ((lst[i]-lst[i-1])<0):
                    z+=3
                elif ((lst[i-1]-lst[i-2])<0) and ((lst[i]-lst[i-1])>0):
                    z+=3
                else:
                    z+=2
            else:
                if ((lst[i-1]-lst[i-2])>0) and ((lst[i]-lst[i-1])<0):
                    z+=1
                elif ((lst[i-1]-lst[i-2])<0) and ((lst[i]-lst[i-1])>0):
                    z+=1
                else:
                    break
        return z