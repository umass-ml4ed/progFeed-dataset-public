# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lis, n)->int:
    count = 0
    for i in range(len(lis)):
        if(len(lis[i])>=n):
            count+=1
        else:
            continue
    return print(count)