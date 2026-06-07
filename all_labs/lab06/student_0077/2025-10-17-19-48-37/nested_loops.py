# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
import random
def get_names(first,last):
    full_names=[]
    for i in first:
        for j in last:
            a= f"{i} {j}"
            full_names.append(a)
    return full_names

def average_scores(lis):
    avr=[]
    for i in lis:
        sum=0
        cnt=0
        for score,late in i:
            if late==0:
                sum+=score
                cnt+=1
            elif late==1:
                sum+=score*0.9
                cnt+=1
            elif late==2:
                sum+=score*0.75
                cnt+=1
            elif late==3:
                sum+=score*0.5
                cnt+=1
            else:
                cnt+=1
                continue
        if cnt>0:
            avr.append(sum/cnt)
        else:
            avr.append(0)
    return avr

