# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lis,n):
    a=0
    for item in lis:
        if len(item)>=n:
            a+=1
    return a
print(count_strings(['','a','aa','aaa'],4))
    

