# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
def count_strings(myString, a):
    cnt=0
    for i in myString:
        if len(i)>=a:
            cnt+=1
    return cnt
