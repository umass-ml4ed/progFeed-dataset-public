#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_zigzag(integers):
    for i in integers:
        if len(integers)<3:
            return True
        if len(integers)>=3:
            for i in range(1, len(integers)-1):
                if (integers[i+1]<integers[i] and integers[i-1]<integers[i]) or (integers[i-1]>integers[i] and integers[i+1]>integers[i+2]):
                    continue
                else:
                    return False
            return True