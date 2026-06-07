# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(l):
    zigzag_count = 0
    if len(l) != 1:
        for index in range(1, len(l)-1):
            if (l[index-1] > l[index] < l[index+1]) or (l[index-1] < l[index] > l[index+1]):
                zigzag_count += 1
        
        if zigzag_count == (len(l)-2):
            return True
        return False
    else:
        return True