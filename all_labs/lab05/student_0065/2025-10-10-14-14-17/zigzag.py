# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(l: list):
        if len(l)<3:
            return True
        for i in range(1, len(l)-1):
            if not ((l[i]>l[i-1] and l[i]>l[i+1]) or (l[i]<l[i-1] and l[i]<l[i+1])):
                return False
        return True
